from django import forms
from django.core.validators import RegexValidator
from .models import Carrito
import re

class FormularioCompra(forms.Form):
    numero_tarjeta = forms.CharField(
        help_text = 'Ingresa los 16 dígitos de tu tarjeta',
        label = 'Número de tu tarjeta de crédito/débito',
        widget = forms.TextInput(
            attrs = {
                'name': 'tarjeta-credito'
            }
        ),
        validators = [
            RegexValidator(
                regex = '^[0-9]{4}((\s[0-9]{4}){3}|([0-9]{4}){3})$',
                message = 'Ingrese un número de tarjeta válido',
                flags = re.RegexFlag.M
            )
        ]
    )

    nombre = forms.CharField(
        help_text = 'Tu nombre en mayúsculas',
        label = 'Nombre',
        widget = forms.TextInput(
            attrs = {
                'name': 'nombre',
                'autocomplete': 'off'
            }
        ),
        validators = [
            RegexValidator(
                regex = '^([A-Z\s+]+)$',
                message = 'Formato de nombre incorrecto',
                flags = re.RegexFlag.M
            )
        ]
    )

    fecha_expiracion = forms.CharField(
        help_text = 'Formato: MM/AA',
        label = 'Expira',
        widget = forms.TextInput(
            attrs = {
                'name': 'fecha_expiracion'
            }
        ),
        validators = [
            RegexValidator(
                regex = '([0-9]\/?){2}',
                message = 'Formato mes/año incorrecto',
                flags = re.RegexFlag.M
            )
        ]
    )

    ccv = forms.CharField(
        help_text = 'Ingresa los tres números que vienen en la parte posterior de tu tarjeta',
        label = 'CCV',
        widget = forms.TextInput(
            attrs = {
                'name': 'ccv',
                'autocomplete': 'off'
            }
        ),
        validators = [
            RegexValidator(
                regex = '^[0-9]{3}$',
                message = '¡El CCV sólo tiene que tener tres números!',
                flags = re.RegexFlag.M
            )
        ]
    )

    def realizar_compra(self, pk):
        carrito = Carrito.objects.get(pk = pk)

        for producto in carrito.listaproducto_set.all():
            print(producto.producto)
