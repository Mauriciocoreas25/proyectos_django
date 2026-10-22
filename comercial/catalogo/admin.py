from django.contrib import admin
from .models import (
    Categoria,
    Producto,
    Tipo_pago,
    Clientes,
    Roles,
    Usuario,
    Venta,
    Detalle_venta,
)

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Tipo_pago)
admin.site.register(Clientes)
admin.site.register(Roles)
admin.site.register(Usuario)
admin.site.register(Venta)
admin.site.register(Detalle_venta)
