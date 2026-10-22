from django.db import models
from .clientes import Clientes
from .usuario import Usuario
from .tipo_pago import Tipo_pago


class Venta(models.Model):
    fecha = models.DateTimeField(verbose_name="Fecha")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='ventas', verbose_name="Cliente")
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ventas', verbose_name="Usuario")
    id_tipo_pago = models.ForeignKey(Tipo_pago, on_delete=models.CASCADE, related_name='ventas', verbose_name="Tipo de pago")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return f"Venta #{self.id} - Total: {self.total} - Fecha: {self.fecha}"
