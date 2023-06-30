from django.urls import path

# Importar settings y static para servir archivos subidos por usuarios.
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    VistaListaCategorias,
    VistaListaSubcategorias,
    VistaListaProductos,
    VistaDetalleProducto,
    VistaAgregarProducto,
    VistaAgregarCategoria,
    VistaAgregarSubcategoria,
    VistaEditarCategoria,
    VistaEditarSubcategoria,
    VistaEditarProducto,
    VistaEliminarCategoria,
    VistaEliminarSubcategoria,
    VistaEliminarProducto
)

urlpatterns = [
    path('', VistaListaCategorias.as_view(), name = 'inicio'),
    path('categorias/nueva/', VistaAgregarCategoria.as_view(), name = 'agregar_categoria'),
    path('categorias/<int:pk>/editar/', VistaEditarCategoria.as_view(), name = 'editar_categoria'),
    path('categorias/<int:pk>/eliminar/', VistaEliminarCategoria.as_view(), name = 'eliminar_categoria'),
    path('categorias/<int:pk>/subcategorias/', VistaListaSubcategorias.as_view(), name = 'lista_subcategorias'),
    path('categorias/<int:pk>/subcategorias/nueva/', VistaAgregarSubcategoria.as_view(), name = 'agregar_subcategoria'),
    path('categorias/<int:pk1>/subcategorias/<int:pk2>/editar/', VistaEditarSubcategoria.as_view(), name = 'editar_subcategoria'),
    path('categorias/<int:pk1>/subcategorias/<int:pk2>/eliminar/', VistaEliminarSubcategoria.as_view(), name = 'eliminar_subcategoria'),
    path('categorias/<int:pk1>/subcategorias/<int:pk2>/productos/', VistaListaProductos.as_view(), name = 'lista_productos'),
    path('categorias/<int:pk1>/subcategorias/<int:pk2>/productos/nuevo/', VistaAgregarProducto.as_view(), name = 'agregar_producto'),
    path('categorias/<int:pk1>/subcategorias/<int:pk2>/productos/<int:pk3>/', VistaDetalleProducto.as_view(), name = 'detalle_producto'),
    path('categorias/<int:pk1>/subcategorias/<int:pk2>/productos/<int:pk3>/editar/', VistaEditarProducto.as_view(), name = 'editar_producto'),
    path('categorias/<int:pk1>/subcategorias/<int:pk2>/productos/<int:pk3>/eliminar/', VistaEliminarProducto.as_view(), name = 'eliminar_producto'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)