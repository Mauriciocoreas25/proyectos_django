from django.db import models
from .ventas import Ventas
from .productos import Productos


class Detalle_ventas(models.Model):
    id_venta = models.ForeignKey(Ventas, on_delete=models.CASCADE, db_column="id_venta", verbose_name="Venta")
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE, db_column="id_producto", verbose_name="Producto")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Unitario")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal")
    created_at = models.DateTimeField(verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalles de Venta"

    def __str__(self):
        return f"Detalle #{self.id} Venta: {self.id_venta_id} Cantidad: {self.cantidad} Subtotal: {self.subtotal}"


# Alias
DetalleVenta = Detalle_ventas
DetalleVentas = Detalle_ventas
