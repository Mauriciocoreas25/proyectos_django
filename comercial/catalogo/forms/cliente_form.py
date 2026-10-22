from django import forms
from django.utils import timezone
from ..models.clientes import Clientes


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre", required=True)
    apellido = forms.CharField(max_length=100, label="Apellido", required=True)
    telefono = forms.CharField(max_length=9, label="Teléfono", required=True)
    correo = forms.EmailField(max_length=150, label="Correo electrónico", required=False)
    direccion = forms.CharField(
        max_length=255,
        label="Dirección",
        required=False,
        widget=forms.Textarea(attrs={"rows": 2})
    )

    def save(self):
        return Clientes.objects.create(
            nombre=self.cleaned_data['nombre'],
            apellido=self.cleaned_data['apellido'],
            telefono=self.cleaned_data['telefono'],
            correo=self.cleaned_data['correo'],
            direccion=self.cleaned_data['direccion'],
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

    def update(self, cliente):
        cliente.nombre = self.cleaned_data['nombre']
        cliente.apellido = self.cleaned_data['apellido']
        cliente.telefono = self.cleaned_data['telefono']
        cliente.correo = self.cleaned_data['correo']
        cliente.direccion = self.cleaned_data['direccion']
        cliente.updated_at = timezone.now()
        cliente.save()
        return cliente
