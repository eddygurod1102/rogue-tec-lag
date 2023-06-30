from django.db import models
from django.conf import settings
from django.urls import reverse

class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=255)
    fotografia = models.FileField(upload_to='categorias')

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('inicio')
    
class Subcategoria(models.Model):
    nombre = models.CharField('Nombre', max_length=255)
    categoria = models.ForeignKey(
        Categoria,
        on_delete = models.CASCADE,
        verbose_name = 'Categoría'
    )
    fotografia = models.FileField(upload_to = 'subcategorias')

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('lista_subcategorias', kwargs = {'pk': self.categoria.pk})

class Producto(models.Model):
    nombre = models.CharField('Nombre del producto', max_length=255)
    descripcion = models.TextField('Descripción', max_length=255)
    categoria = models.ForeignKey(
        Subcategoria,
        on_delete = models.CASCADE,
        verbose_name = 'Categoría'
    )
    fotografia = models.FileField(upload_to = 'productos')
    stock = models.SmallIntegerField('Stock', default = 0)
    precio = models.DecimalField('Precio', max_digits = 7, decimal_places = 2, default = 0)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse(
            'lista_productos',
            kwargs = {
                'pk1': self.categoria.categoria.pk,
                'pk2': self.categoria.pk
            }
        )

class Comentario(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete = models.CASCADE,
        verbose_name = 'Producto'
    )

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        verbose_name = 'Usuario'
    )

    comentario = models.TextField(max_length = 255)

    def __str__(self):
        return self.comentario