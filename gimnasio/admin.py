from django.contrib import admin
from .models import Categoria, Producto, Subcategoria, Comentario

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Subcategoria)
admin.site.register(Comentario)