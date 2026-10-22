from django.db import models
from .venta import Venta
from .producto import Producto


class Detalle_venta(models.Model):
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles', verbose_name="Venta")
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='detalles', verbose_name="Producto")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio unitario")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return f"Detalle #{self.id} Venta #{self.id_venta_id} - Producto #{self.id_producto_id} Cant: {self.cantidad}"
