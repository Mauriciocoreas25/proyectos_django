from django.shortcuts import render
from catalogo.models.categoria import Categoria

# Create your views here.

def lista_categorias(request):
    categorias_bd = Categoria.objects.all()
    if categorias_bd.exists():
        categorias = categorias_bd
    else:
        categorias = [
            {
                'id': 1,
                'nombre': 'tv',
                'descripcion': 'Televisores de alta gama'
            },
            {
                'id': 2,
                'nombre': 'Laptop',
                'descripcion': 'Computadoras portátiles'
            },
        ]
    return render(request, "categoria/lista.html", context={
        'categorias': categorias
    })