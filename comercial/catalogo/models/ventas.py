from django.db import models
from .clientes import Clientes
from .usuarios import Usuarios
from .tipo_pago import Tipo_pago


class Ventas(models.Model):
    fecha = models.DateTimeField(verbose_name="Fecha")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, db_column="id_cliente", verbose_name="Cliente")
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, db_column="id_usuario", verbose_name="Usuario")
    id_tipo_pago = models.ForeignKey(Tipo_pago, on_delete=models.CASCADE, db_column="id_tipo_pago", verbose_name="Tipo de Pago")
    created_at = models.DateTimeField(verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return f"Venta #{self.id} Fecha: {self.fecha} Total: {self.total}"


# Alias
Venta = Ventas
