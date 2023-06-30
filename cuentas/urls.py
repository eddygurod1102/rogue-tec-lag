from django.urls import path
from .views import (
    VistaInicioSesion,
    VistaCerrarSesion,
    VistaCrearUsuario,
    VistaCambiarContraseña,
    VistaResetearContraseña,
    VistaResetearContraseñaHecho,
    VistaResetearContraseñaConfirmar,
)

urlpatterns = [
    path('login/', VistaInicioSesion.as_view(), name = 'login'),
    path('logout/', VistaCerrarSesion.as_view(), name = 'logout'),
    path('signin/', VistaCrearUsuario.as_view(), name ='signin'),
    path('cambiar_contrasena/', VistaCambiarContraseña.as_view(), name = 'cambiar_contrasena'),
    path('resetear_contrasena/', VistaResetearContraseña.as_view(), name = 'resetear_contrasena'),
    path('resetear_contrasena_hecho/', VistaResetearContraseñaHecho.as_view(), name = 'resetear_contrasena_hecho'),
    path('resetear_contrasena/<uidb64>/<token>/', VistaResetearContraseñaConfirmar.as_view(), name = 'resetear_contrasena_confirmar'),
]