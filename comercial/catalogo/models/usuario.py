from django.db import models
from .roles import Roles


class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True, verbose_name="Usuario")
    password = models.CharField(max_length=255, verbose_name="Contraseña")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    telefono = models.CharField(max_length=9, verbose_name="Teléfono")
    correo = models.CharField(max_length=150, null=True, blank=True, verbose_name="Correo")
    id_rol = models.ForeignKey(Roles, on_delete=models.CASCADE, related_name='usuarios', verbose_name="Rol")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return f"id: {self.id} Usuario: {self.username} - {self.nombre} {self.apellido}"
