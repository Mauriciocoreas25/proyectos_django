from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views.inicio import inicio
from .views.home import home
from .views.registrarUsuario import registraUsuario
from .views.categoria import (
    lista_categorias,
    delete_categoria,
    add_categoria,
    update_categoria,
)
from .views.tipo_pago import (
    lista_tipos_pago,
    delete_tipo_pago,
    add_tipo_pago,
    update_tipo_pago,
)
from .views.cliente import (
    lista_clientes,
    delete_cliente,
    add_cliente,
    update_cliente,
)
from .views.rol import (
    lista_roles,
    delete_rol,
    add_rol,
    update_rol,
)
from .views.producto import (
    lista_productos,
    delete_producto,
    add_producto,
    update_producto,
    generar_pdf_view,
)

urlpatterns = [
    # Inicio & Home (Semana 14)
    path("", inicio, name="inicio"),
    path("home/", home, name="home"),

    # Autenticación y Registro (Semana 14)
    path("login/", LoginView.as_view(template_name="login/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registrar/", registraUsuario, name="registrar_usuario"),
    path("registrar_usuario/", registraUsuario),

    # Reporte PDF (Semana 14)
    path("reporte_productos/", generar_pdf_view, name="reporte_producto"),

    # Categorías (Semanas 11 y 12)
    path("categoria/", lista_categorias, name="list_categoria"),
    path("categoria/lista/", lista_categorias, name="list_categorias"),
    path("categoria/agregar/", add_categoria, name="add_categoria"),
    path("categoria/actualizar/<int:id>/", update_categoria, name="update_categoria"),
    path("categoria/eliminar/<int:id>/", delete_categoria, name="delete_categoria"),

    # Productos (Semana 13)
    path("producto/", lista_productos, name="list_producto"),
    path("producto/agregar/", add_producto, name="add_producto"),
    path("producto/actualizar/<int:id>/", update_producto, name="update_producto"),
    path("producto/eliminar/<int:id>/", delete_producto, name="delete_producto"),

    # Tipos de Pago (Semana 10)
    path("tipo-pago/", lista_tipos_pago, name="list_tipo_pago"),
    path("tipo-pago/agregar/", add_tipo_pago, name="add_tipo_pago"),
    path("tipo-pago/actualizar/<int:id>/", update_tipo_pago, name="update_tipo_pago"),
    path("tipo-pago/eliminar/<int:id>/", delete_tipo_pago, name="delete_tipo_pago"),

    # Clientes (Semana 10)
    path("cliente/", lista_clientes, name="list_cliente"),
    path("cliente/agregar/", add_cliente, name="add_cliente"),
    path("cliente/actualizar/<int:id>/", update_cliente, name="update_cliente"),
    path("cliente/eliminar/<int:id>/", delete_cliente, name="delete_cliente"),

    # Roles (Semanas 10 y 14)
    path("rol/", lista_roles, name="list_rol"),
    path("rol/agregar/", add_rol, name="add_rol"),
    path("rol/actualizar/<int:id>/", update_rol, name="update_rol"),
    path("rol/eliminar/<int:id>/", delete_rol, name="delete_rol"),
]
