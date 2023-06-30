from .models import Comentario
from django.forms import ModelForm

class FormularioComentario(ModelForm):
    class Meta():
        model = Comentario
        fields = ['comentario']