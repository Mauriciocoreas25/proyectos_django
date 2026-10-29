from django.shortcuts import render, redirect, get_object_or_404
from ..models.rol import Rol
from ..forms.rol_form import RolForm


def lista_roles(request):
    roles = Rol.objects.all()
    return render(request, "rol/lista.html", context={
        'roles': roles
    })


def delete_rol(request, id):
    rol = get_object_or_404(Rol, id=id)
    rol.delete()
    return redirect('list_rol')


def add_rol(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_rol')
        else:
            return render(request, "rol/add.html", context={'form': form})
    return render(request, "rol/add.html", context={'form': RolForm()})


def update_rol(request, id):
    rol = get_object_or_404(Rol, id=id)
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.update(rol)
            return redirect('list_rol')
        else:
            return render(request, "rol/update.html", context={
                'form': form,
                'rol': rol
            })
    form = RolForm(initial={
        'nombre': rol.nombre,
        'descripcion': rol.descripcion,
    })
    return render(request, "rol/update.html", context={
        'form': form,
        'rol': rol
    })
