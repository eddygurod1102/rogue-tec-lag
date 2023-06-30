from django.template import Library
from django.shortcuts import get_object_or_404
from sales.models import *

register = Library()

@register.inclusion_tag('etiquetas/productos_carrito.html')
def carrito(usuario):
    try:
        carrito = Carrito.objects.get(usuario = usuario)
    except Carrito.DoesNotExist:
        carrito = Carrito(usuario = usuario)
        carrito.save()

    numero_productos = ListaProducto.objects.filter(carrito = carrito).count()

    return {
        'numero_productos': numero_productos,
        'user': usuario,
    }
    # carrito = get_object_or_404(Carrito, usuario = usuario)
    # try:
    #     numero_productos = ListaProducto.objects.filter(carrito = carrito).count()
    # except Carrito.DoesNotExist:
    #     carrito_nuevo = Carrito(usuario = usuario)
    #     carrito_nuevo.save()
    #     numero_productos = ListaProducto.objects.filter(carrito = carrito_nuevo).count()

    #     return {
    #         'numero_productos': numero_productos,
    #         'user': usuario,
    #     }
    # else:
    #     return {
    #         'numero_productos': numero_productos,
    #         'user': usuario,
    #     }

@register.simple_tag
def total(carrito):
    productos = ListaProducto.objects.filter(carrito = carrito)
    precio = 0

    for producto in productos:
        precio = precio + producto.cantidad * producto.producto.precio

    return precio