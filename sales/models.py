from django.db import models
from django.conf import settings
from gimnasio.models import Producto

# Create your models here.
class Carrito(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        verbose_name = 'Usuario'
    )

    def __str__(self):
        return f'Carrito de {self.usuario}'


class ListaProducto(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete = models.CASCADE,
        verbose_name = 'Producto'
    )

    carrito = models.ForeignKey(
        Carrito,
        on_delete = models.CASCADE,
        verbose_name = 'Carrito'
    )

    cantidad = models.SmallIntegerField('Cantidad', default = 0)

    def __str__(self):
        return f'{self.producto} - {self.carrito}'

    # Calcula el precio total del carrito.
    def precio_total(usuario):
        pass