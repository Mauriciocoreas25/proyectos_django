# 📚 Guía Maestra de Estudio: Django Framework (Semanas 10 a 13)
> **Materia:** Desarrollo de Aplicaciones Web / Frameworks  
> **Proyecto:** Sistema Comercial (`comercial`)  
> **Enfoque:** Preparación para el Examen Teórico-Práctico

---

## 🧭 Mapa de Contenidos por Semana

* **Semana 10:** Fundamentos, patrón MVT, modularización de `models/` y `views/`, conexión MySQL, migraciones (`makemigrations`, `migrate`), Django Shell y modelo `Categoria`.
* **Semana 11:** Relaciones entre tablas (`ForeignKey`), `related_name`, `on_delete=models.CASCADE`, fechas automáticas (`auto_now_add` vs `auto_now`), soporte de imágenes con `Pillow`.
* **Semana 12:** Managers y consultas del ORM (`filter`, lookups `__gt`, `__icontains`), herencia de plantillas (`base.html`, `{% extends %}`, `{% block %}`), Tailwind CSS, Crispy Forms y CRUD completo.
* **Semana 13:** Relaciones en formularios (`ModelChoiceField`), validaciones personalizadas con `clean()`, subida y borrado de imágenes con `request.FILES` y `storage.delete()`, paginación de datos con `Paginator`.

---

## 1. Arquitectura MVT y Organización del Proyecto

### ¿Qué es el patrón MVT de Django?
A diferencia del clásico MVC (Modelo-Vista-Controlador), Django implementa **MVT**:
1. **Model (Modelo):** Define la estructura de los datos, reglas de negocio y traduce clases de Python en tablas de base de datos a través del ORM.
2. **View (Vista):** Es el intermediario lógico (equivalente al *Controlador* en MVC). Recibe la petición HTTP (`request`), consulta los Modelos y decide qué plantilla renderizar pasando los datos por contexto (`context`).
3. **Template (Plantilla):** Capa visual (HTML + Django Template Language - DTL). Muestra la información al usuario final.

### Flujo de una Petición HTTP en Django:
1. El usuario entra a `http://127.0.0.1:8000/producto/`.
2. `comercial/urls.py` deriva la petición a `catalogo/urls.py`.
3. `catalogo/urls.py` ejecuta la función de vista asociada: `lista_productos(request)`.
4. La vista consulta los datos: `Producto.objects.all()`.
5. El ORM traduce la consulta a SQL: `SELECT * FROM catalogo_producto`.
6. La vista recibe los objetos y ejecuta: `render(request, "producto/lista.html", {'productos': productos})`.
7. El motor DTL procesa la plantilla HTML con los datos y entrega el HTML completo al navegador.

### La regla de oro de la estructura modular (`models/` y `views/`)
En proyectos reales no se deja todo en un solo `models.py` o `views.py`. Se crean paquetes (carpetas):
* `catalogo/models/`: Cada modelo en su archivo (`categoria.py`, `producto.py`, etc.).
* **Regla obligatoria:** En `catalogo/models/__init__.py` se **deben** importar las clases:
  ```python
  from .categoria import Categoria
  from .producto import Producto
  from .tipo_pago import Tipo_pago
  from .clientes import Clientes
  from .roles import Roles
  ```
  > **Nota de Examen:** Si no importas el modelo en `__init__.py`, Django y el comando `makemigrations` **no detectarán la clase** y no crearán las tablas en la base de datos.

---

## 2. Modelos, Campos y Base de Datos (Semanas 10 y 11)

### Tipos de Campos Frecuentes en Examen
| Campo Django | Tipo SQL | Uso principal | Argumentos típicos |
| :--- | :--- | :--- | :--- |
| `models.CharField` | `VARCHAR(N)` | Textos cortos (nombres, títulos) | `max_length=100`, `null=True`, `blank=True` |
| `models.TextField` | `TEXT` / `LONGTEXT` | Descripciones o textos extensos | `null=True`, `blank=True` |
| `models.DecimalField`| `DECIMAL(M, D)` | Dinero, precios, subtotales | `max_digits=10`, `decimal_places=2` |
| `models.IntegerField`| `INT` | Números enteros positivos o negativos | `default=0` |
| `models.PositiveIntegerField` | `INT UNSIGNED` | Stock, cantidades (no permite negativos) | `default=0` |
| `models.DateTimeField` | `DATETIME` | Marcas de tiempo de creación/edición | `auto_now_add=True`, `auto_now=True` |
| `models.ImageField` | `VARCHAR(255)` | Ruta de la imagen en disco | `upload_to='productos/'`, `null=True` |
| `models.ForeignKey` | `INT` (FK) | Relaciones 1 a N | `on_delete=models.CASCADE`, `related_name='...'` |

### Diferencia crucial: `auto_now_add` vs `auto_now`
* `auto_now_add=True`: Guarda la fecha y hora **únicamente al crear el registro por primera vez**. Ideal para `created_at`.
* `auto_now=True`: Actualiza la fecha y hora **cada vez que el objeto se guarda o modifica (`.save()`)**. Ideal para `updated_at`.

### Relaciones entre tablas (`ForeignKey`)
En `catalogo/models/producto.py`:
```python
class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        related_name='productos', 
        verbose_name="Categoria"
    )
```
* `on_delete=models.CASCADE`: Si se elimina la categoría, se eliminan automáticamente todos sus productos asociados.
* `related_name='productos'`: Permite la consulta inversa desde la categoría hacia sus productos (`mi_categoria.productos.all()`).

---

## 3. Migraciones y Conexión MySQL

### Configuración en `settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'comercial',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### ¿Qué hace cada comando de migración?
```bash
python manage.py makemigrations
```
* Inspecciona los modelos definidos en las aplicaciones instaladas.
* Compara el estado actual con el historial previo y genera un archivo de migración en Python (ej: `0001_initial.py`). **No altera la base de datos todavía**.

```bash
python manage.py migrate
```
* Lee los archivos de migración pendientes y **ejecuta el código SQL real en el motor de base de datos** (crea tablas, índices, columnas). Registra las migraciones aplicadas en la tabla interna `django_migrations`.

---

## 4. El ORM de Django y Consultas con Managers (Semana 12 P1)

El objeto `.objects` es el **Manager** por defecto que permite interactuar con la base de datos sin escribir SQL directo.

### Métodos Principales del Manager
```python
# 1. Obtener todos los registros (QuerySet)
productos = Producto.objects.all()

# 2. Obtener un único registro por clave primaria o condición
# Nota: Si no existe lanza DoesNotExist; si hay más de uno lanza MultipleObjectsReturned
producto = Producto.objects.get(id=1) 
producto = Producto.objects.get(pk=1)

# 3. Primer y último elemento (según ordenamiento)
primero = Producto.objects.first()
ultimo = Producto.objects.last()

# 4. Conteo de registros
total = Producto.objects.count()

# 5. Creación directa en base de datos
nuevo = Categoria.objects.create(
    nombre="Accesorios", 
    descripcion="Dispositivos periféricos"
)

# 6. Eliminar un registro
producto.delete()

# 7. Actualizar un registro
producto.precio_venta = 899.99
producto.save()
```

### Filtros (`filter`) y Field Lookups
```python
# Buscar por coincidencia exacta
Producto.objects.filter(categoria__nombre="Laptop")

# Operadores de comparación (Field Lookups usando doble guion bajo '__')
Producto.objects.filter(stock__gt=5)         # stock > 5 (Greater Than)
Producto.objects.filter(stock__gte=10)       # stock >= 10 (Greater Than or Equal)
Producto.objects.filter(stock__lt=3)         # stock < 3 (Less Than)
Producto.objects.filter(stock__lte=0)        # stock <= 0 (Less Than or Equal)
Producto.objects.filter(nombre__contains="USB")   # Contiene texto (case-sensitive)
Producto.objects.filter(nombre__icontains="laptop") # Contiene texto ignorando mayúsculas
Producto.objects.filter(nombre__startswith="Mem")  # Empieza con
Producto.objects.filter(precio_venta__range=(100, 500)) # Entre 100 y 500

# Consultas combinadas (AND)
Producto.objects.filter(stock__gte=5, precio_venta__lte=100)

# Consulta inversa con related_name
cat = Categoria.objects.get(id=1)
productos_de_la_categoria = cat.productos.all()
```

---

## 5. Plantillas y Django Template Language (DTL) (Semana 12 P2)

### Herencia de Plantillas
Permite definir una plantilla maestra (`base.html`) con el diseño global y dejar bloques que las demás páginas rellenan.

**En `templates/base.html`:**
```html
<!doctype html>
<html lang="es">
<head>
    <title>Comercial - {% block titulo %}{% endblock titulo %}</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body>
    <nav>...</nav>
    <main>
        {% block contenido %}
        {% endblock contenido %}
    </main>
</body>
</html>
```

**En `catalogo/templates/categoria/lista.html`:**
```html
{% extends "base.html" %}

{% block titulo %}Lista de Categorías{% endblock titulo %}

{% block contenido %}
    <h1>Categorías</h1>
    {% if categorias %}
        <ul>
            {% for cat in categorias %}
                <li>{{ cat.id }} - {{ cat.nombre }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No hay registros disponibles.</p>
    {% endif %}
{% endblock contenido %}
```

### Etiquetas y Filtros de Plantilla
* Variables: `{{ variable.atributo }}`
* Etiquetas de control: `{% if condicion %} ... {% else %} ... {% endif %}`, `{% for item in lista %} ... {% endfor %}`
* Generación de URLs dinámicas por nombre: `{% url 'nombre_ruta' %}` o con parámetro: `{% url 'update_categoria' cat.id %}`
* Filtros comunes:
  * `{{ nombre|lower }}`: convierte a minúsculas.
  * `{{ nombre|upper }}`: convierte a mayúsculas.
  * `{{ texto|truncatewords:30 }}`: corta a 30 palabras.
  * `{{ fecha|date:"d/m/Y" }}`: formatea fechas.

---

## 6. Formularios Django y Carga de Archivos (Semanas 12 P2 y 13 P1)

### Formularios con `forms.Form`
En `catalogo/forms/producto_form.py`:
```python
from django import forms
from django.core.validators import FileExtensionValidator
from ..models.producto import Producto
from ..models.categoria import Categoria

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    precio_compra = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0)
    precio_venta = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0)
    stock = forms.IntegerField(min_value=0)
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        label="Categoría",
        empty_label="Seleccione una categoría"
    )
    imagen = forms.ImageField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg"])]
    )

    # Validación personalizada entre campos
    def clean(self):
        cleaned_data = super().clean()
        compra = cleaned_data.get('precio_compra')
        venta = cleaned_data.get('precio_venta')
        if compra and venta and venta <= compra:
            self.add_error('precio_venta', 'El precio de venta debe superar al de compra.')
        return cleaned_data
```

### Reglas críticas para subir archivos/imágenes en Django
1. **En el formulario HTML:** El tag `<form>` DEBE tener el atributo `enctype="multipart/form-data"`:
   ```html
   <form method="post" enctype="multipart/form-data">
       {% csrf_token %}
       {{ form|crispy }}
       <button type="submit">Guardar</button>
   </form>
   ```
2. **En la vista (`views.py`):** Se debe pasar tanto `request.POST` como `request.FILES`:
   ```python
   form = ProductoForm(request.POST, request.FILES)
   ```
3. **En `settings.py`:**
   ```python
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'
   ```

---

## 7. Paginación de Datos (Semana 13 P2)

### En la Vista (`catalogo/views/producto.py`)
```python
from django.core.paginator import Paginator

def lista_productos(request):
    # 1. Obtenemos el QuerySet ordenado
    productos = Producto.objects.all().order_by('id')
    # 2. Inicializamos el paginador (ej. 10 productos por página)
    paginador = Paginator(productos, 10)
    # 3. Leemos el número de página de los parámetros GET (?page=2)
    pagina = request.GET.get('page')
    # 4. Obtenemos el objeto Page seguro (si no existe, entrega la pág 1)
    productos_paginados = paginador.get_page(pagina)
    
    return render(request, "producto/lista.html", {'productos': productos_paginados})
```

### En el Template (`producto/lista.html`)
```html
<nav>
    {% if productos.has_previous %}
        <a href="?page=1">Primera</a>
        <a href="?page={{ productos.previous_page_number }}">Anterior</a>
    {% endif %}

    <span>Página {{ productos.number }} de {{ productos.paginator.num_pages }}</span>

    {% if productos.has_next %}
        <a href="?page={{ productos.next_page_number }}">Siguiente</a>
        <a href="?page={{ productos.paginator.num_pages }}">Última</a>
    {% endif %}
</nav>
```

---

## 8. Simulación de Preguntas de Examen (Autoevaluación)

### Pregunta 1
**¿Cuál es la diferencia entre ejecutar `python manage.py makemigrations` y `python manage.py migrate`?**
> **Respuesta:** `makemigrations` analiza los cambios en el código Python de los modelos y genera un archivo de migración que describe esos cambios. `migrate` toma esos archivos de migración y ejecuta los comandos SQL en el motor de base de datos para crear o alterar las tablas físicas.

### Pregunta 2
**Si se divide `models.py` en varios archivos dentro de una carpeta `models/`, ¿qué archivo obligatorio se debe crear y qué debe contener?**
> **Respuesta:** Se debe crear el archivo `__init__.py` dentro de la carpeta `models/` y en él se deben importar todos los modelos (`from .categoria import Categoria`, etc.). De lo contrario, Django no registrará las clases en su catálogo de modelos.

### Pregunta 3
**¿Para qué sirve el atributo `related_name` en una relación `ForeignKey`?**
> **Respuesta:** Permite definir el nombre del descriptor de relación inversa. Por ejemplo, en `categoria = models.ForeignKey(Categoria, related_name='productos')`, permite consultar desde una categoría todos sus productos mediante `mi_categoria.productos.all()`.

### Pregunta 4
**¿Por qué un formulario HTML que sube imágenes debe incluir obligatoriamente `enctype="multipart/form-data"` y qué parámetro se pasa a la vista en Django?**
> **Respuesta:** El atributo `enctype="multipart/form-data"` le indica al navegador que no codifique los datos como texto plano, sino en fragmentos binarios para transmitir el archivo. En la vista de Django, se debe instanciar el formulario pasando `request.FILES` junto con `request.POST` (ej: `Form(request.POST, request.FILES)`).

### Pregunta 5
**En el sistema de plantillas DTL, ¿cuál es la diferencia entre `{% block %}` y `{% extends %}`?**
> **Respuesta:** `{% extends "base.html" %}` se utiliza al inicio de una plantilla hija para heredar toda la estructura HTML de la plantilla padre. `{% block nombre %}` define secciones dentro de la plantilla que pueden ser reemplazadas o personalizadas por las plantillas hijas.
