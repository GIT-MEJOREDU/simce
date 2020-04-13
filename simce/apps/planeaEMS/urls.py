from django.urls import path
from .views import listarTurnosEscolares, listarCiclosEscolares, listarExtensionesEms, listarCentrosTrabajo, \
    datos_escuela

urlpatterns = [
    path('listar_turnosescolares/',listarTurnosEscolares, name = 'listar_turnosescolares'),
    path('listar_ciclosescolares/',listarCiclosEscolares, name = 'listar_ciclosescolares'),
    path('listar_extensionesems/',listarExtensionesEms, name = 'listar_extensionesems'),
    path('listar_centrostrabajo/',listarCentrosTrabajo, name = 'listar_centrostrabajo'),
    path('datos_escuela/',datos_escuela, name = 'datos_escuela'),
]