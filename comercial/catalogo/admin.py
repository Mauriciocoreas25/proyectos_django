from django.contrib import admin
from .models import Categoria, Tipo_pago, Clientes, Roles

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Tipo_pago)
admin.site.register(Clientes)
admin.site.register(Roles)
