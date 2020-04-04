from django.urls import path
from .views import listarTurnosEscolares, listarCiclosEscolares, listarExtensionesEms, listarCentrosTrabajo, listarEntidades

urlpatterns = [
    path('listar_turnosescolares/',listarTurnosEscolares, name = 'listar_turnosescolares'),
    path('listar_ciclosescolares/',listarCiclosEscolares, name = 'listar_ciclosescolares'),
    path('listar_extensionesems/',listarExtensionesEms, name = 'listar_extensionesems'),
    path('listar_centrostrabajo/',listarCentrosTrabajo, name = 'listar_centrostrabajo'),
    path('listar_entidades/', listarEntidades, name='listar_entidades')
]