from django.urls import path
<<<<<<< HEAD
from .views import listarTurnosEscolares, listarCiclosEscolares, listarExtensionesEms, listarCentrosTrabajo, \
    datos_escuela
=======
from .views import listarTurnosEscolares, listarCiclosEscolares, listarExtensionesEms, listarCentrosTrabajo, listarEntidades
>>>>>>> isag

urlpatterns = [
    path('listar_turnosescolares/',listarTurnosEscolares, name = 'listar_turnosescolares'),
    path('listar_ciclosescolares/',listarCiclosEscolares, name = 'listar_ciclosescolares'),
    path('listar_extensionesems/',listarExtensionesEms, name = 'listar_extensionesems'),
    path('listar_centrostrabajo/',listarCentrosTrabajo, name = 'listar_centrostrabajo'),
<<<<<<< HEAD
    path('datos_escuela/',datos_escuela, name = 'datos_escuela'),
=======
    path('listar_entidades/', listarEntidades, name='listar_entidades')
>>>>>>> isag
]