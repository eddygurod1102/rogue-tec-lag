from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Carrito, ListaProducto
from gimnasio.models import Producto
from .forms import FormularioCompra

# Vista que muestra los productos en un carrito.
class VistaListaCarrito(LoginRequiredMixin, ListView):
    login_url = '/cuentas/login'
    model = Carrito
    template_name = 'sales/lista/lista_carrito.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrito'] = Carrito.objects.get(usuario = self.kwargs['pk'])
        context['precios'] = ListaProducto.objects.aggregate(Sum('producto__precio'))
        return context
    
# Agregar objectos al carrito de un usuario (Es necesario iniciar sesión para
# agregar productos al carrito. Si el usuario no tiene una sesión iniciada, se le
# redirigirá al formulario de inicio de sesión).
@login_required(login_url = '/cuentas/login')
def agregar_carrito(request, pk):
    # Obtener la cantidad de un producto.
    cantidad = int(request.POST.get('cantidad', True))
    print(cantidad)

    # Obtener el producto.
    producto = Producto.objects.get(pk = pk)

    # Verificar si la cantidad de productos a mandar al carrito es mayor al stock
    # disponible del producto. No tiene sentido agarrar 6 productos en stock si sólo
    # hay 5, por ejemplo.
    if cantidad > producto.stock:
        pass
    else:
        # Obtener el carrito del usuario
        carrito = Carrito.objects.get(usuario = request.user)
        # print(request.user)
        # Verificar si el producto a mandar al carro ya existe en la lista
        # de productos.
        if ListaProducto.objects.filter(carrito = carrito, producto = producto).count() == 1:
            # Para que un producto no aparezca dos veces en la lista, sólo incrementamos la
            # cantidad que el usuario mandó al carrito.
            lista = ListaProducto.objects.get(carrito = carrito, producto = producto)
            lista.cantidad = lista.cantidad + cantidad
            lista.save()
        else:
            # En caso de que no existe ese producto en el carrito del usuario, lo agregamos
            # a su lista.
            lista = ListaProducto(
                carrito = carrito,
                producto = producto,
                cantidad = cantidad
            )

            lista.save()

    return HttpResponseRedirect(reverse('inicio'))

# Vista que muestra el formulario de compra
class VistaFormularioCompra(FormView):
    model = Carrito
    template_name = 'sales/formulario/compra.html'
    form_class = FormularioCompra
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrito'] = Carrito.objects.get(pk = self.kwargs['pk'])
        return context


def comprar(request, pk):
    carrito = Carrito.objects.get(pk = pk)
    for producto_set in carrito.listaproducto_set.all():
        producto = Producto.objects.get(pk = producto_set.producto.pk)
        producto.stock = producto.stock - producto_set.cantidad
        producto.save()
        producto_set.delete()

    return HttpResponseRedirect(reverse('inicio'))