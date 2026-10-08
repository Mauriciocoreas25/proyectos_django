from django.db import models


class Tipo_pago(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    descripcion = models.CharField(max_length=255, null=True, blank=True, verbose_name="Descripción")
    created_at = models.DateTimeField(verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Tipo de Pago"
        verbose_name_plural = "Tipos de Pago"

    def __str__(self):
        return f"id: {self.id} Nombre: {self.nombre}"


# Alias para compatibilidad con convenciones CamelCase
TipoPago = Tipo_pago
