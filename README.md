# Sistema Comercial - Django (Semana 10)

Proyecto desarrollado para la materia de Desarrollo de Aplicaciones Web / Frameworks, correspondiente a la **Semana 10: Práctica 1 y Práctica 2**.

## 📌 Contenido de las Prácticas

### Práctica 1: Primer Proyecto Django y Patrón MVT
* Creación del proyecto `comercial` y la aplicación `catalogo`.
* Implementación de la arquitectura modular para `models` y `views`.
* Configuración del modelo `Categoria`.
* Creación de la vista `lista_categorias` y paso de datos mediante contexto.
* Plantilla HTML con renderizado dinámico mediante bucles `{% for %}` (`templates/categoria/lista.html`).
* Enrutamiento de URLs a nivel de app y a nivel de proyecto.

### Práctica 2: Conexión con Base de Datos MySQL y Migraciones
* Conexión con servidor MySQL (`Laragon` / `MariaDB`) utilizando el conector `mysqlclient`.
* Generación y aplicación de migraciones (`makemigrations` y `migrate`).
* Manipulación de datos desde la consola interactiva `Django Shell`.
* **Ejercicios de Práctica del Sistema Comercial:**
  1. `Tipo_pago`
  2. `Clientes`
  3. `Roles`
* Modelos complementarios del diagrama: `Usuarios`, `Productos`, `Ventas` y `Detalle_ventas`.
* Registro de todos los modelos en el panel de administración de Django (`admin.py`).

---

## 🚀 Requisitos e Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Mauriciocoreas25/proyectos_django.git
   cd proyectos_django
   ```

2. **Crear y activar el entorno virtual:**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r comercial/requirements.txt
   ```

4. **Configurar la base de datos:**
   * Asegúrate de tener tu servidor MySQL activo (por ejemplo, en Laragon o XAMPP).
   * Crear la base de datos `comercial`:
     ```sql
     CREATE DATABASE comercial;
     ```
   * Verificar credenciales en `comercial/comercial/settings.py`.

5. **Aplicar migraciones:**
   ```bash
   cd comercial
   python manage.py migrate
   ```

6. **Iniciar el servidor:**
   ```bash
   python manage.py runserver
   ```

7. **Rutas disponibles:**
   * Catálogo de categorías: `http://127.0.0.1:8000/categoria/`
   * Panel de administración: `http://127.0.0.1:8000/admin/`
