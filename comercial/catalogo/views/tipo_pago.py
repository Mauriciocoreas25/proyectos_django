from django.shortcuts import render, redirect, get_object_or_404
from ..models.tipo_pago import Tipo_pago
from ..forms.tipo_pago_form import TipoPagoForm


def lista_tipos_pago(request):
    tipos_pago = Tipo_pago.objects.all()
    return render(request, "tipo_pago/lista.html", context={
        'tipos_pago': tipos_pago
    })


def delete_tipo_pago(request, id):
    tipo_pago = get_object_or_404(Tipo_pago, id=id)
    tipo_pago.delete()
    return redirect('list_tipo_pago')


def add_tipo_pago(request):
    if request.method == 'POST':
        form = TipoPagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tipo_pago')
        else:
            return render(request, "tipo_pago/add.html", context={'form': form})
    return render(request, "tipo_pago/add.html", context={'form': TipoPagoForm()})


def update_tipo_pago(request, id):
    tipo_pago = get_object_or_404(Tipo_pago, id=id)
    if request.method == 'POST':
        form = TipoPagoForm(request.POST)
        if form.is_valid():
            form.update(tipo_pago)
            return redirect('list_tipo_pago')
        else:
            return render(request, "tipo_pago/update.html", context={
                'form': form,
                'tipo_pago': tipo_pago
            })
    form = TipoPagoForm(initial={
        'nombre': tipo_pago.nombre,
        'descripcion': tipo_pago.descripcion
    })
    return render(request, "tipo_pago/update.html", context={
        'form': form,
        'tipo_pago': tipo_pago
    })
