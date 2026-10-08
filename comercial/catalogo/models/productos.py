from django.db import models
from .categoria import Categoria


class Productos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.CharField(max_length=255, null=True, blank=True, verbose_name="Descripción")
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de compra")
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de venta")
    stock = models.IntegerField(verbose_name="Stock")
    imagen = models.CharField(max_length=255, null=True, blank=True, verbose_name="Imagen")
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column="id_categoria", verbose_name="Categoría")
    created_at = models.DateTimeField(verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"id: {self.id} Nombre: {self.nombre} Stock: {self.stock}"


# Alias
Producto = Productos
