from django.shortcuts import render
# Imports
from .models import Turnosescolares,Ciclosescolares,Extensionesems

# Create your views here.
def Home(request):
        return render(request,'index.html')

def listarTurnosEscolares(request):
        turnosescolares = Turnosescolares.objects.using('dimensionesPlaneaEms').all()
        ciclosescolares = Ciclosescolares.objects.using('dimensionesPlaneaEms').all()
        extensionesems = Extensionesems.objects.using('dimensionesPlaneaEms').all()
        return render(request, 'planeaEMS/listar_turnosescolares.html',{'turnosescolares':turnosescolares,'ciclosescolares':ciclosescolares,'extensionesems':extensionesems})