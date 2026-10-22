from django.shortcuts import render, redirect, get_object_or_404
from ..models.clientes import Clientes
from ..forms.cliente_form import ClienteForm


def lista_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, "cliente/lista.html", context={
        'clientes': clientes
    })


def delete_cliente(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    cliente.delete()
    return redirect('list_cliente')


def add_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_cliente')
        else:
            return render(request, "cliente/add.html", context={'form': form})
    return render(request, "cliente/add.html", context={'form': ClienteForm()})


def update_cliente(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.update(cliente)
            return redirect('list_cliente')
        else:
            return render(request, "cliente/update.html", context={
                'form': form,
                'cliente': cliente
            })
    form = ClienteForm(initial={
        'nombre': cliente.nombre,
        'apellido': cliente.apellido,
        'telefono': cliente.telefono,
        'correo': cliente.correo,
        'direccion': cliente.direccion,
    })
    return render(request, "cliente/update.html", context={
        'form': form,
        'cliente': cliente
    })
