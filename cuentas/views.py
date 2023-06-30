from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
)
from django.views.generic import CreateView
from django.urls import reverse
from .forms import FormularioUsuario

# Vista para iniciar sesión.
class VistaInicioSesion(LoginView):
    template_name = 'cuentas/formularios/login.html'

# Vista para cerrar sesión.
class VistaCerrarSesion(LogoutView):
    pass

# Vista para el registro de un nuevo usuario.
class VistaCrearUsuario(CreateView):
    form_class = FormularioUsuario
    template_name = 'cuentas/formularios/crear_usuario.html'
    success_url = '/'

# Vista para cambiar la contraseña de un usuario.
class VistaCambiarContraseña(PasswordChangeView):
    template_name = 'cuentas/formularios/cambiar_contrasena.html'
    success_url = '/'

# Vista para resetea una contraseña. Se enviará correo al email del usuario.
class VistaResetearContraseña(PasswordResetView):
    template_name = 'cuentas/formularios/resetear_contrasena.html'
    email_template_name = 'cuentas/formularios/resetear_contrasena_email.html'
    html_email_template_name = 'cuentas/formularios/resetear_contrasena_email.html'
    subject_template_name = 'cuentas/asunto.txt'
    success_url = '/cuentas/resetear_contrasena_hecho'

class VistaResetearContraseñaHecho(PasswordResetDoneView):
    template_name = 'cuentas/resetear_contrasena_hecho.html'

class VistaResetearContraseñaConfirmar(PasswordResetConfirmView):
    template_name = 'cuentas/formularios/resetear_contrasena.confirmar.html'
    success_url = '/cuentas/login/'