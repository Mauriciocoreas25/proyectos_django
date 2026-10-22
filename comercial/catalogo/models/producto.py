from django.db import models
from .categoria import Categoria


class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(max_length=255, null=True, blank=True, verbose_name="Descripción")
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de compra")
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de venta")
    stock = models.PositiveIntegerField(verbose_name="Stock")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos', verbose_name="Categoria")
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True, verbose_name="Imagen")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return f"id: {self.id} Nombre: {self.nombre} Precio de compra: {self.precio_compra} Precio de venta: {self.precio_venta} Stock: {self.stock}"
