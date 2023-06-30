from django.urls import path
from .views import VistaListaCarrito, agregar_carrito, VistaFormularioCompra, comprar

urlpatterns = [
    path('carrito/<int:pk>/', VistaListaCarrito.as_view(), name = 'lista_carrito'),
    path('agregar_carrito/<int:pk>/', agregar_carrito, name = 'agregar_carrito'),
    path('carrito/<int:pk>/compra/', VistaFormularioCompra.as_view(), name = 'compra'),
    path('carrito/<int:pk>/comprar/', comprar, name = 'comprar'),
]