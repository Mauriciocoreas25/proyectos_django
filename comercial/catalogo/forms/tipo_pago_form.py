from django import forms
from django.utils import timezone
from ..models.tipo_pago import Tipo_pago


class TipoPagoForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre", required=True)
    descripcion = forms.CharField(
        max_length=255,
        label="Descripción",
        required=False,
        widget=forms.Textarea(attrs={"rows": 3})
    )

    def save(self):
        return Tipo_pago.objects.create(
            nombre=self.cleaned_data['nombre'],
            descripcion=self.cleaned_data['descripcion'],
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

    def update(self, tipo_pago):
        tipo_pago.nombre = self.cleaned_data['nombre']
        tipo_pago.descripcion = self.cleaned_data['descripcion']
        tipo_pago.updated_at = timezone.now()
        tipo_pago.save()
        return tipo_pago
