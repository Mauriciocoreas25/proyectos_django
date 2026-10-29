from .categoria import (
    lista_categorias,
    add_categoria,
    update_categoria,
    delete_categoria,
)
from .tipo_pago import (
    lista_tipos_pago,
    add_tipo_pago,
    update_tipo_pago,
    delete_tipo_pago,
)
from .cliente import (
    lista_clientes,
    add_cliente,
    update_cliente,
    delete_cliente,
)
from .rol import (
    lista_roles,
    add_rol,
    update_rol,
    delete_rol,
)
from .producto import (
    lista_productos,
    add_producto,
    update_producto,
    delete_producto,
    generar_pdf_view,
)
from .inicio import inicio
from .home import home
from .registrarUsuario import registraUsuario

__all__ = [
    'lista_categorias',
    'add_categoria',
    'update_categoria',
    'delete_categoria',
    'lista_tipos_pago',
    'add_tipo_pago',
    'update_tipo_pago',
    'delete_tipo_pago',
    'lista_clientes',
    'add_cliente',
    'update_cliente',
    'delete_cliente',
    'lista_roles',
    'add_rol',
    'update_rol',
    'delete_rol',
    'lista_productos',
    'add_producto',
    'update_producto',
    'delete_producto',
    'generar_pdf_view',
    'inicio',
    'home',
    'registraUsuario',
]
