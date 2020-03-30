from django.urls import path
from .views import listarTurnosEscolares

urlpatterns = [
    path('listar_turnosescolares/',listarTurnosEscolares, name = 'listar_turnosescolares'),
]