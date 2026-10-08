from django.db import models

# Create your models here.

class Categoria(models.Model):
    # define un campo de tipo texto con maximo de 255 caracteres
    nombre = models.TextField(max_length=255, verbose_name="Nombre")
    # define un campo de tipo texto que puede ser nulo con maximo de 255 caracteres
    descripcion = models.TextField(max_length=255, null=True, blank=True, verbose_name="Descripción")
    # define campos de tipo fecha y hora para almacenar la fecha de creacion y actualización del registro
    created_at = models.DateTimeField(verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(verbose_name="Fecha de actualización")

    # function que muestra la informacion de la tabla en consola
    def __str__(self):
        return f"id: {self.id} Nombre: {self.nombre} Descripcion: {self.descripcion} Fecha de creación : {self.created_at} Fecha de actualización {self.updated_at}"