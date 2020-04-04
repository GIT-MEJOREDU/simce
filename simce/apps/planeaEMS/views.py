from django.shortcuts import render
# Imports
from .models import Turnosescolares,Ciclosescolares,Extensionesems, Centrostrabajo, EntidadesFederativas

# Create your views here.
def Home(request):
        return render(request,'index.html')

def listarTurnosEscolares(request):
        turnosescolares = Turnosescolares.objects.using('dimensionesPlaneaEms').all()
        return render(request, 'planeaEMS/listar_turnosescolares.html',{'turnosescolares':turnosescolares})

def listarCiclosEscolares(request):
        ciclosescolares = Ciclosescolares.objects.using('dimensionesPlaneaEms').all()
        return render(request, 'planeaEMS/listar_ciclosescolares.html',{'ciclosescolares':ciclosescolares})

def listarExtensionesEms(request):
        extensionesems = Extensionesems.objects.using('dimensionesPlaneaEms').all()
        return render(request, 'planeaEMS/listar_extensionesems.html',{'extensionesems':extensionesems})

def listarCentrosTrabajo(request):
        centrostrabajo = Centrostrabajo.objects.using('dimensionesPlaneaEms').all()
        ciclosescolares = Ciclosescolares.objects.using('dimensionesPlaneaEms').all()
        return render(request, 'planeaEMS/listar_centrostrabajo.html',{'ciclosescolares':ciclosescolares,'centrostrabajo':centrostrabajo})


def listarEntidades(request):
        entidadesfederativas = EntidadesFederativas.objects.using('dimensionesPlaneaEms').all().iterator()
        return render(request, 'planeaEMS/entidades.html',{'entidadesfederativas': entidadesfederativas})