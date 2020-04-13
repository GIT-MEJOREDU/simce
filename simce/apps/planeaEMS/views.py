from django.shortcuts import render
# Imports
from .models import Turnosescolares,Ciclosescolares,Extensionesems, Centrostrabajo, EntidadesFederativas

# Create your views here.
def datos_escuela(request, cct = '01DCT0279R', turno_escolar = 1, ciclo_escolar = 19,extension_ems = 0):
        #recibe información de la escuela a consultar
        from django.db import connection
        #Se genera la consulta, y se agregan los parámetros a la consulta con el método format()
        query_string = 'SELECT ct."cNombreCentroTrabajo", ct."cClaveCentroTrabajo", te."cNombreTurnoEscolar", ex."cNombreExtensionEms", ex."iPkExtensionEms", pl."cClavePlantel", ss."cNombreSubsistemaEms", ef."cNombreEntidad", ef."iPkEntidadFederativa", ss."iPkSubsistemaEms" \
                FROM hechos."hechosReporteEmsInee" AS h \
                FULL OUTER JOIN "dimensionesPlaneaEms"."centrosTrabajo" AS ct ON ct."iPkCentroTrabajo" = h."iFkCentroTrabajo" \
		        FULL OUTER JOIN "dimensionesPlaneaEms"."turnosEscolares" AS te ON te."iPkTurnoEscolar" = h."iFkTurnoEscolar" \
		        FULL OUTER JOIN "dimensionesPlaneaEms"."extensionesEms" AS ex ON ex."iPkExtensionEms" = h."iFkExtensionEms" \
		        FULL OUTER JOIN "dimensionesPlaneaEms"."plantelesEms" AS pl ON pl."iPkPlantel" = h."iFkPlantel" \
		        FULL OUTER JOIN "dimensionesPlaneaEms"."subsistemasEms" AS ss ON ss."iPkSubsistemaEms" = h."iFkSubsistemaEms" \
		        FULL OUTER JOIN "dimensionesPlaneaEms"."entidadesFederativas" AS ef ON ef."iPkEntidadFederativa" =h."iFkEntidadFederativa" \
                WHERE ct."cClaveCentroTrabajo"=\'{p1}\' AND te."iPkTurnoEscolar"={p2} AND h."iFkCicloEscolar"={p3} AND ex."iPkExtensionEms">={p4}'.format(p1=cct,p2=turno_escolar,p3=ciclo_escolar,p4=extension_ems)
        with connection.cursor() as cursor:
            cursor.execute(query_string)
            rawData = cursor.fetchall()
            result = []
            for r in rawData:
                result.append(list(r))

        #se obtienen datos de nivel de dominio en LyC
        extension_ems = result[0][4] #se obtiene dato de la consulta de datos de escuela
        query_string = 'SELECT ce."cCicloEscolar" AS "CicloEscolar", \
                CASE WHEN h."dPorcentAlumnsEscNvlLgrILyC" = -9999 THEN -0.01 ELSE CAST(h."dPorcentAlumnsEscNvlLgrILyC" AS NUMERIC (5,2))   END AS "I_Insuficiente", \
		CASE WHEN h."dPorcentAlumnsEscNvlLgrIILyC" = -9999 THEN -0.01 ELSE CAST(h."dPorcentAlumnsEscNvlLgrIILyC" AS NUMERIC (5,2))  END AS "II_Elemental", \
		CASE WHEN h."dPorcentAlumnsEscNvlLgrIIILyC" = -9999 THEN -0.01 ELSE CAST(h."dPorcentAlumnsEscNvlLgrIIILyC" AS NUMERIC (5,2)) END AS "III_Bueno", \
		CASE WHEN h."dPorcentAlumnsEscNvlLgrIVLyC"  = -9999 THEN -0.01 ELSE CAST(h."dPorcentAlumnsEscNvlLgrIVLyC" AS NUMERIC (5,2))  END AS "IV_Excelente" \
		FROM hechos."hechosReporteEmsInee" AS h \
		FULL OUTER JOIN "dimensionesPlaneaEms"."centrosTrabajo"  AS ct ON ct."iPkCentroTrabajo" = h."iFkCentroTrabajo" \
		FULL OUTER JOIN "dimensionesPlaneaEms"."turnosEscolares" AS te ON te."iPkTurnoEscolar" = h."iFkTurnoEscolar" \
		FULL OUTER JOIN "dimensionesPlaneaEms"."ciclosEscolares" AS ce ON ce."iPkCicloEscolar" = h."iFkCicloEscolar" \
		FULL OUTER JOIN "dimensionesPlaneaEms"."extensionesEms"  AS ex ON ex."iPkExtensionEms" = h."iFkExtensionEms" \
		WHERE ct."cClaveCentroTrabajo"=\'{p1}\' AND te."iPkTurnoEscolar"={p2} AND h."iFkCicloEscolar" IN ({p3}) AND \
                ex."iPkExtensionEms" = {p4} AND h."dPorcentAlumnsEscNvlLgrILyC" >= 0'.format(p1=cct,p2=turno_escolar,p3=ciclo_escolar,p4=extension_ems)
        with connection.cursor() as cursor:
            cursor.execute(query_string)
            rawData = cursor.fetchall()
            result_lyc = []
            for r in rawData:
                result_lyc.append(list(r))
        
        contexto = {'consulta': result,'consulta_lyc':result_lyc} #parametro que se envía al html

        return render(request,'planeaEMS/datos_escuela.html',contexto)

def Home(request):
        return render(request,'index.html')

def listarTurnosEscolares(request):
        turnosescolares = Turnosescolares.objects.using('dimensionesPlaneaEms').all().iterator() 
        return render(request, 'planeaEMS/listar_turnosescolares.html',{'turnosescolares':turnosescolares})

def listarCiclosEscolares(request):
        ciclosescolares = Ciclosescolares.objects.using('dimensionesPlaneaEms').all().iterator()
        return render(request, 'planeaEMS/listar_ciclosescolares.html',{'ciclosescolares':ciclosescolares})

def listarExtensionesEms(request):
        extensionesems = Extensionesems.objects.using('dimensionesPlaneaEms').all().order_by('-ipkextensionems').iterator()
        return render(request, 'planeaEMS/listar_extensionesems.html',{'extensionesems':extensionesems})

def listarCentrosTrabajo(request):
        centrostrabajo = Centrostrabajo.objects.using('dimensionesPlaneaEms').all().iterator()
        ciclosescolares = Ciclosescolares.objects.using('dimensionesPlaneaEms').all().iterator()
        return render(request, 'planeaEMS/listar_centrostrabajo.html',{'ciclosescolares':ciclosescolares,'centrostrabajo':centrostrabajo})


def listarEntidades(request):
        entidadesfederativas = EntidadesFederativas.objects.using('dimensionesPlaneaEms').all().iterator()
        return render(request, 'planeaEMS/entidades.html',{'entidadesfederativas': entidadesfederativas})

