from django.template import Library
from gimnasio.models import Categoria

register = Library()

@register.inclusion_tag('etiquetas/categorias.html')
def categorias():
    categorias = Categoria.objects.all().order_by('nombre')

    return {
        'categorias': categorias
    }