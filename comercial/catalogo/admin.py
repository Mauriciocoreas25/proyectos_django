from django.contrib import admin
from .models import (
    Categoria,
    Producto,
    Tipo_pago,
    Clientes,
    Rol,
    Usuario,
)

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Tipo_pago)
admin.site.register(Clientes)
admin.site.register(Rol)
admin.site.register(Usuario)
