from django.shortcuts import render, redirect, get_object_or_404
from ..models.categoria import Categoria
from ..forms.categoria_form import CategoriaForm

# Create your views here.


def lista_categorias(request):
    lista = Categoria.objects.all()
    return render(request, "categoria/lista.html", context={
        'categorias': lista
    })


def delete_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('list_categoria')


def add_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_categoria')
        else:
            return render(request, "categoria/add.html", context={
                'form': form
            })
    return render(request, "categoria/add.html", context={
        'form': CategoriaForm()
    })


def update_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.update(categoria)
            return redirect('list_categoria')
        else:
            return render(request, "categoria/update.html", context={
                'form': form,
                'categoria': categoria
            })

    form = CategoriaForm(initial={
        'nombre': categoria.nombre,
        'descripcion': categoria.descripcion
    })
    return render(request, "categoria/update.html", context={
        'form': form,
        'categoria': categoria
    })
