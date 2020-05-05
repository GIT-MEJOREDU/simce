from django.shortcuts import render
import json
from decimal import Decimal

# Imports
from .models import Turnosescolares, Ciclosescolares, Extensionesems, Centrostrabajo, EntidadesFederativas

# Create your views here.


def nivel_logro(request, cct='01DCT0279R', turno_escolar=1, ciclo_escolar=19, extension_ems=0):
    # recibe información de la escuela a consultar
    from django.db import connection
    # Se genera la consulta, y se agregan los parámetros a la consulta con el método format()
    query_string = 'SELECT ct."cNombreCentroTrabajo", ct."cClaveCentroTrabajo", te."cNombreTurnoEscolar", ex."cNombreExtensionEms", ex."iPkExtensionEms", pl."cClavePlantel", ss."cNombreSubsistemaEms", ef."cNombreEntidad", ef."iPkEntidadFederativa", ss."iPkSubsistemaEms" \
                FROM hechos."hechosReporteEmsInee" AS h \
                FULL OUTER JOIN "dimensionesPlaneaEms"."centrosTrabajo" AS ct ON ct."iPkCentroTrabajo" = h."iFkCentroTrabajo" \
		        FULL OUTER JOIN "dimensionesPlaneaEms"."turnosEscolares" AS te ON te."iPkTurnoEscolar" = h."iFkTurnoEscolar" \
		        FULL OUTER JOIN "dimensionesPlaneaEms"."extensionesEms" AS ex ON ex."iPkExtensionEms" = h."iFkExtensionEms" \
		        FULL OUTER JOIN "dimensionesPlaneaEms"."plantelesEms" AS pl ON pl."iPkPlantel" = h."iFkPlantel" \
		        FULL OUTER JOIN "dimensionesPlaneaEms"."subsistemasEms" AS ss ON ss."iPkSubsistemaEms" = h."iFkSubsistemaEms" \
		        FULL OUTER JOIN "dimensionesPlaneaEms"."entidadesFederativas" AS ef ON ef."iPkEntidadFederativa" =h."iFkEntidadFederativa" \
                WHERE ct."cClaveCentroTrabajo"=\'{p1}\' AND te."iPkTurnoEscolar"={p2} AND h."iFkCicloEscolar"={p3} AND ex."iPkExtensionEms">={p4}'.format(p1=cct, p2=turno_escolar, p3=ciclo_escolar, p4=extension_ems)
    with connection.cursor() as cursor:
        cursor.execute(query_string)
        rawData = cursor.fetchall()
        result = []
        for r in rawData:
            result.append(list(r))

    # se obtienen datos de nivel de dominio en LyC
    # se obtiene dato de la consulta de datos de escuela
    extension_ems = result[0][4]
    query_string = 'SELECT \'LyC\' AS "Area", \
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
                ex."iPkExtensionEms" = {p4} AND h."dPorcentAlumnsEscNvlLgrILyC" >= 0 \
                UNION ALL \
                SELECT  \'Mat\' AS "Area", \
			CASE WHEN h."dPorcentAlumnsEscNvlLgrIMat"   = -9999 THEN -0.01 ELSE CAST(h."dPorcentAlumnsEscNvlLgrIMat" AS NUMERIC (5,2))   END AS "I_Insuficiente", \
			CASE WHEN h."dPorcentAlumnsEscNvlLgrIIMat"  = -9999 THEN -0.01 ELSE CAST(h."dPorcentAlumnsEscNvlLgrIIMat" AS NUMERIC (5,2))  END AS "II_Elemental", \
			CASE WHEN h."dPorcentAlumnsEscNvlLgrIIIMat" = -9999 THEN -0.01 ELSE CAST(h."dPorcentAlumnsEscNvlLgrIIIMat" AS NUMERIC (5,2)) END AS "III_Bueno", \
			CASE WHEN h."dPorcentAlumnsEscNvlLgrIVMat"  = -9999 THEN -0.01 ELSE CAST(h."dPorcentAlumnsEscNvlLgrIVMat" AS NUMERIC (5,2))  END AS "IV_Excelente" \
		FROM hechos."hechosReporteEmsInee" AS h \
		FULL OUTER JOIN "dimensionesPlaneaEms"."centrosTrabajo"  AS ct ON ct."iPkCentroTrabajo" = h."iFkCentroTrabajo" \
		FULL OUTER JOIN "dimensionesPlaneaEms"."turnosEscolares" AS te ON te."iPkTurnoEscolar" = h."iFkTurnoEscolar" \
		FULL OUTER JOIN "dimensionesPlaneaEms"."ciclosEscolares" AS ce ON ce."iPkCicloEscolar" = h."iFkCicloEscolar" \
		FULL OUTER JOIN "dimensionesPlaneaEms"."extensionesEms"  AS ex ON ex."iPkExtensionEms" = h."iFkExtensionEms" \
		WHERE ct."cClaveCentroTrabajo"=\'{p1}\' AND te."iPkTurnoEscolar"={p2} AND h."iFkCicloEscolar" IN ({p3}) AND ex."iPkExtensionEms" = {p4} \
		AND h."dPorcentAlumnsEscNvlLgrIMat"   >= 0'.format(p1=cct, p2=turno_escolar, p3=ciclo_escolar, p4=extension_ems)
    with connection.cursor() as cursor:
        cursor.execute(query_string)
        rawData = cursor.fetchall()
        print("rawData")
        print(rawData)
        result_logro = []
        for r in rawData:
            result_logro.append(list(r))

    # se convierten decimales a cadena
    # Se elimina el cast Decimal('999.99') que tiene cada valor decimal que existe en al consulta
    # print(result_logro[0][1])
    cont1 = 0
    cont2 = 0
    for i in result_logro:
        for item in i:
            # print(item)
            result_logro[cont1][cont2] = str(item)
            cont2 = cont2 + 1
        cont1 = cont1 + 1
        cont2 = 0

  #  El arreglo de Arreglos [[],[],...] se convierte a un arrego con formato JSON [{},{},...]
    results_as_dict = []
    # print(result_logro)
    for i in result_logro:
        result_as_dict = {
            "Area_de_Dominio": i[0],
            "Nivel_I_Dominio_insuficiente": i[1],
            "Nivel_II_Dominio_básico": i[2],
            "Nivel_III_Dominio_satisfactorio": i[3],
            "Nivel_IV_Dominio_sobresaliente": i[4]
        }
        # print("results_as_dict")
        # print(result_as_dict)
        results_as_dict.append(result_as_dict)

    # print("results_as_dict")
    # print(results_as_dict)

    # print("result")
    # print(result_logro)
    #json_logro = json.dumps(results_as_dict)
    #print("result_as_dict")
    #print(results_as_dict)
    # print("json")
    # print(json_logro)
    # parametro que se envía al html
    contexto = {'consulta': result, 'consulta_logro': results_as_dict}
    return render(request, 'planeaEMS/nivel_logro.html', contexto)


def datos_escuela(request, cct='01DCT0279R', turno_escolar=1, ciclo_escolar=19, extension_ems=0):
    # recibe información de la escuela a consultar
    from django.db import connection
    # Se genera la consulta, y se agregan los parámetros a la consulta con el método format()
    query_string = 'SELECT ct."cNombreCentroTrabajo", ct."cClaveCentroTrabajo", te."cNombreTurnoEscolar", ex."cNombreExtensionEms", ex."iPkExtensionEms", pl."cClavePlantel", ss."cNombreSubsistemaEms", ef."cNombreEntidad", ef."iPkEntidadFederativa", ss."iPkSubsistemaEms" \
                FROM hechos."hechosReporteEmsInee" AS h \
                FULL OUTER JOIN "dimensionesPlaneaEms"."centrosTrabajo" AS ct ON ct."iPkCentroTrabajo" = h."iFkCentroTrabajo" \
		        FULL OUTER JOIN "dimensionesPlaneaEms"."turnosEscolares" AS te ON te."iPkTurnoEscolar" = h."iFkTurnoEscolar" \
		        FULL OUTER JOIN "dimensionesPlaneaEms"."extensionesEms" AS ex ON ex."iPkExtensionEms" = h."iFkExtensionEms" \
		        FULL OUTER JOIN "dimensionesPlaneaEms"."plantelesEms" AS pl ON pl."iPkPlantel" = h."iFkPlantel" \
		        FULL OUTER JOIN "dimensionesPlaneaEms"."subsistemasEms" AS ss ON ss."iPkSubsistemaEms" = h."iFkSubsistemaEms" \
		        FULL OUTER JOIN "dimensionesPlaneaEms"."entidadesFederativas" AS ef ON ef."iPkEntidadFederativa" =h."iFkEntidadFederativa" \
                WHERE ct."cClaveCentroTrabajo"=\'{p1}\' AND te."iPkTurnoEscolar"={p2} AND h."iFkCicloEscolar"={p3} AND ex."iPkExtensionEms">={p4}'.format(p1=cct, p2=turno_escolar, p3=ciclo_escolar, p4=extension_ems)
    with connection.cursor() as cursor:
        cursor.execute(query_string)
        rawData = cursor.fetchall()
        result = []
        for r in rawData:
            result.append(list(r))

    # se obtienen datos de nivel de dominio en LyC
    # se obtiene dato de la consulta de datos de escuela
    extension_ems = result[0][4]
    query_string = 'SELECT \'LyC\' AS "Area", \
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
                ex."iPkExtensionEms" = {p4} AND h."dPorcentAlumnsEscNvlLgrILyC" >= 0 \
                UNION ALL \
                SELECT  \'Mat\' AS "Area", \
			CASE WHEN h."dPorcentAlumnsEscNvlLgrIMat"   = -9999 THEN -0.01 ELSE CAST(h."dPorcentAlumnsEscNvlLgrIMat" AS NUMERIC (5,2))   END AS "I_Insuficiente", \
			CASE WHEN h."dPorcentAlumnsEscNvlLgrIIMat"  = -9999 THEN -0.01 ELSE CAST(h."dPorcentAlumnsEscNvlLgrIIMat" AS NUMERIC (5,2))  END AS "II_Elemental", \
			CASE WHEN h."dPorcentAlumnsEscNvlLgrIIIMat" = -9999 THEN -0.01 ELSE CAST(h."dPorcentAlumnsEscNvlLgrIIIMat" AS NUMERIC (5,2)) END AS "III_Bueno", \
			CASE WHEN h."dPorcentAlumnsEscNvlLgrIVMat"  = -9999 THEN -0.01 ELSE CAST(h."dPorcentAlumnsEscNvlLgrIVMat" AS NUMERIC (5,2))  END AS "IV_Excelente" \
		FROM hechos."hechosReporteEmsInee" AS h \
		FULL OUTER JOIN "dimensionesPlaneaEms"."centrosTrabajo"  AS ct ON ct."iPkCentroTrabajo" = h."iFkCentroTrabajo" \
		FULL OUTER JOIN "dimensionesPlaneaEms"."turnosEscolares" AS te ON te."iPkTurnoEscolar" = h."iFkTurnoEscolar" \
		FULL OUTER JOIN "dimensionesPlaneaEms"."ciclosEscolares" AS ce ON ce."iPkCicloEscolar" = h."iFkCicloEscolar" \
		FULL OUTER JOIN "dimensionesPlaneaEms"."extensionesEms"  AS ex ON ex."iPkExtensionEms" = h."iFkExtensionEms" \
		WHERE ct."cClaveCentroTrabajo"=\'{p1}\' AND te."iPkTurnoEscolar"={p2} AND h."iFkCicloEscolar" IN ({p3}) AND ex."iPkExtensionEms" = {p4} \
		AND h."dPorcentAlumnsEscNvlLgrIMat"   >= 0'.format(p1=cct, p2=turno_escolar, p3=ciclo_escolar, p4=extension_ems)
    with connection.cursor() as cursor:
        cursor.execute(query_string)
        rawData = cursor.fetchall()
        result_lyc = []
        for r in rawData:
            result_lyc.append(list(r))

    # parametro que se envía al html
    contexto = {'consulta': result, 'consulta_lyc': result_lyc}

    return render(request, 'planeaEMS/datos_escuela.html', contexto)


def Home(request):
    return render(request, 'index.html')


def listarTurnosEscolares(request):
    turnosescolares = Turnosescolares.objects.using(
        'dimensionesPlaneaEms').all().iterator()
    return render(request, 'planeaEMS/listar_turnosescolares.html', {'turnosescolares': turnosescolares})


def listarCiclosEscolares(request):
    ciclosescolares = Ciclosescolares.objects.using(
        'dimensionesPlaneaEms').all().iterator()
    return render(request, 'planeaEMS/listar_ciclosescolares.html', {'ciclosescolares': ciclosescolares})


def listarExtensionesEms(request):
    extensionesems = Extensionesems.objects.using(
        'dimensionesPlaneaEms').all().order_by('-ipkextensionems').iterator()
    return render(request, 'planeaEMS/listar_extensionesems.html', {'extensionesems': extensionesems})


def listarCentrosTrabajo(request):
    centrostrabajo = Centrostrabajo.objects.using(
        'dimensionesPlaneaEms').all().iterator()
    ciclosescolares = Ciclosescolares.objects.using(
        'dimensionesPlaneaEms').all().iterator()
    return render(request, 'planeaEMS/listar_centrostrabajo.html', {'ciclosescolares': ciclosescolares, 'centrostrabajo': centrostrabajo})


def listarEntidades(request):
    entidadesfederativas = EntidadesFederativas.objects.using(
        'dimensionesPlaneaEms').all().iterator()
    return render(request, 'planeaEMS/entidades.html', {'entidadesfederativas': entidadesfederativas})
