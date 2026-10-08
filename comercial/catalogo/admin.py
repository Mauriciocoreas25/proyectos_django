from django.contrib import admin
from .models import (
    Categoria,
    Tipo_pago,
    Clientes,
    Roles,
    Usuarios,
    Productos,
    Ventas,
    Detalle_ventas,
)

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Tipo_pago)
admin.site.register(Clientes)
admin.site.register(Roles)
admin.site.register(Usuarios)
admin.site.register(Productos)
admin.site.register(Ventas)
admin.site.register(Detalle_ventas)
