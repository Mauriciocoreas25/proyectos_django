from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import HttpResponse

from ..models.producto import Producto
from ..forms.producto_form import ProductoForm


@login_required
def lista_productos(request):
    usuario = request.user
    if usuario.rol.nombre != 'admin':
        return redirect('home')
    productos = Producto.objects.all().order_by('id')
    paginador = Paginator(productos, 10)
    pagina = request.GET.get('page')
    productos_paginados = paginador.get_page(pagina)
    return render(request, "producto/lista.html", context={
        'productos': productos_paginados
    })


@login_required
def delete_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if producto.imagen:
        storage = producto.imagen.storage
        if storage.exists(producto.imagen.name):
            storage.delete(producto.imagen.name)
    producto.delete()
    return redirect('list_producto')


@login_required
def add_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_producto')
        else:
            return render(request, "producto/add.html", context={
                'form': form
            })
    return render(request, "producto/add.html", context={
        'form': ProductoForm()
    })


@login_required
def update_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.update(producto)
            return redirect('list_producto')
        else:
            return render(request, "producto/update.html", context={
                'form': form,
                'producto': producto
            })

    form = ProductoForm(initial={
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'precio_compra': producto.precio_compra,
        'precio_venta': producto.precio_venta,
        'stock': producto.stock,
        'categoria': producto.categoria,
        'imagen': producto.imagen,
    })
    return render(request, "producto/update.html", context={
        'form': form,
        'producto': producto
    })


def generar_pdf_view(request):
    # 1. Obtener datos o contexto
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    # 2. Renderizar el HTML con los datos
    html_string = render_to_string('producto/reporte.html', contexto)

    # 3. Convertir HTML a PDF con WeasyPrint
    try:
        from weasyprint import HTML
        pdf = HTML(string=html_string).write_pdf()
        # 4. Enviar la respuesta HTTP indicando que es un PDF
        response = HttpResponse(pdf, content_type='application/pdf')
        # 'inline' para vista previa, 'attachment' para descargar
        response['Content-Disposition'] = 'inline; filename="documento.pdf"'
        return response
    except Exception:
        # Vista previa en HTML si no están configuradas las librerías nativas Pango/GTK en Windows
        return HttpResponse(html_string)
