from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.models import User

class FormularioUsuario(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)