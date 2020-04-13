#from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']

class Turnosescolares(models.Model):
    ipkturnoescolar = models.IntegerField(db_column='iPkTurnoEscolar', primary_key=True)  # Field name made lowercase.
    cnombreturnoescolar = models.CharField(db_column='cNombreTurnoEscolar', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turnosEscolares'
        db_tablespace = 'dimensionesPlaneaEms'

class Ciclosescolares(models.Model):
    ipkcicloescolar = models.IntegerField(db_column='iPkCicloEscolar', primary_key=True)  # Field name made lowercase.
    ccicloescolar = models.CharField(db_column='cCicloEscolar', max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciclosEscolares'
        db_tablespace = 'dimensionesPlaneaEms'

class Extensionesems(models.Model):
    ipkextensionems = models.IntegerField(db_column='iPkExtensionEms', primary_key=True)  # Field name made lowercase.
    cnombreextensionems = models.CharField(db_column='cNombreExtensionEms', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'extensionesEms'# This is an auto-generated Django model module.
        db_tablespace = 'dimensionesPlaneaEms'

class Centrostrabajo(models.Model):
    ipkcentrotrabajo = models.IntegerField(db_column='iPkCentroTrabajo', primary_key=True)  # Field name made lowercase.
    cclavecentrotrabajo = models.CharField(db_column='cClaveCentroTrabajo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cnombrecentrotrabajo = models.CharField(db_column='cNombreCentroTrabajo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iindescuelaconpuntajematlyc = models.IntegerField(db_column='iIndEscuelaConPuntajeMatLyC', blank=True, null=True)  # Field name made lowercase.
    dlatitud = models.DecimalField(db_column='dLatitud', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    dlongitud = models.DecimalField(db_column='dLongitud', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    the_geom = models.GeometryField(blank=True, null=True)  # This field type is a guess.
    cescuelaparecida = models.CharField(db_column='cEscuelaParecida', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'centrosTrabajo'
        db_tablespace = 'dimensionesPlaneaEms'

class Hechosreporteemsinee(models.Model):
    ifkcentrotrabajo = models.IntegerField(db_column='iFkCentroTrabajo', blank=True, null=True)  # Field name made lowercase.
    #ipkcentrotrabajo = models.ForeignKey('Centrostrabajo', on_delete=models.CASCADE)
    ifkcicloescolar = models.IntegerField(db_column='iFkCicloEscolar', blank=True, null=True)  # Field name made lowercase.
    ifkturnoescolar = models.IntegerField(db_column='iFkTurnoEscolar', blank=True, null=True)  # Field name made lowercase.
    ifknivelescolar = models.IntegerField(db_column='iFkNivelEscolar', blank=True, null=True)  # Field name made lowercase.
    ifkentidadfederativa = models.IntegerField(db_column='iFkEntidadFederativa', blank=True, null=True)  # Field name made lowercase.
    ifkmunicipio = models.IntegerField(db_column='iFkMunicipio', blank=True, null=True)  # Field name made lowercase.
    ifklocalidad = models.IntegerField(db_column='iFkLocalidad', blank=True, null=True)  # Field name made lowercase.
    ifkgradomarginacionplanea = models.IntegerField(db_column='iFkGradoMarginacionPlanea', blank=True, null=True)  # Field name made lowercase.
    ifkextensionems = models.IntegerField(db_column='iFkExtensionEms', blank=True, null=True)  # Field name made lowercase.
    ifksubsistemaems = models.IntegerField(db_column='iFkSubsistemaEms', blank=True, null=True)  # Field name made lowercase.
    ifktiposostenimiento = models.IntegerField(db_column='iFkTipoSostenimiento', blank=True, null=True)  # Field name made lowercase.
    ifkresultadolyc = models.IntegerField(db_column='iFkResultadoLyC', blank=True, null=True)  # Field name made lowercase.
    ifkresultadomat = models.IntegerField(db_column='iFkResultadoMat', blank=True, null=True)  # Field name made lowercase.
    ifkescalacontexto = models.IntegerField(db_column='iFkEscalaContexto', blank=True, null=True)  # Field name made lowercase.
    ifkplantel = models.IntegerField(db_column='iFkPlantel', blank=True, null=True)  # Field name made lowercase.
    ifktipomuestra = models.IntegerField(db_column='iFkTipoMuestra', blank=True, null=True)  # Field name made lowercase.
    iadvertenciafiabilidadlyc = models.IntegerField(db_column='iAdvertenciaFiabilidadLyC', blank=True, null=True)  # Field name made lowercase.
    iadvertenciafiabilidadmat = models.IntegerField(db_column='iAdvertenciaFiabilidadMat', blank=True, null=True)  # Field name made lowercase.
    ialumnosevaluadoslyc = models.IntegerField(db_column='iAlumnosEvaluadosLyC', blank=True, null=True)  # Field name made lowercase.
    ialumnosevaluadosmat = models.IntegerField(db_column='iAlumnosEvaluadosMat', blank=True, null=True)  # Field name made lowercase.
    dpuntajepromedioesclyc = models.FloatField(db_column='dPuntajePromedioEscLyC', blank=True, null=True)  # Field name made lowercase.
    ialumnosescnvllgrilyc = models.IntegerField(db_column='iAlumnosEscNvlLgrILyC', blank=True, null=True)  # Field name made lowercase.
    ialumnosescnvllgriilyc = models.IntegerField(db_column='iAlumnosEscNvlLgrIILyC', blank=True, null=True)  # Field name made lowercase.
    ialumnosescnvllgriiilyc = models.IntegerField(db_column='iAlumnosEscNvlLgrIIILyC', blank=True, null=True)  # Field name made lowercase.
    ialumnosescnvllgrivlyc = models.IntegerField(db_column='iAlumnosEscNvlLgrIVLyC', blank=True, null=True)  # Field name made lowercase.
    dporcentalumnsescnvllgrilyc = models.FloatField(db_column='dPorcentAlumnsEscNvlLgrILyC', blank=True, null=True)  # Field name made lowercase.
    dporcentalumnsescnvllgriilyc = models.FloatField(db_column='dPorcentAlumnsEscNvlLgrIILyC', blank=True, null=True)  # Field name made lowercase.
    dporcentalumnsescnvllgriiilyc = models.FloatField(db_column='dPorcentAlumnsEscNvlLgrIIILyC', blank=True, null=True)  # Field name made lowercase.
    dporcentalumnsescnvllgrivlyc = models.FloatField(db_column='dPorcentAlumnsEscNvlLgrIVLyC', blank=True, null=True)  # Field name made lowercase.
    dpuntajepromedioescmat = models.FloatField(db_column='dPuntajePromedioEscMat', blank=True, null=True)  # Field name made lowercase.
    ialumnosescnvllgrimat = models.IntegerField(db_column='iAlumnosEscNvlLgrIMat', blank=True, null=True)  # Field name made lowercase.
    ialumnosescnvllgriimat = models.IntegerField(db_column='iAlumnosEscNvlLgrIIMat', blank=True, null=True)  # Field name made lowercase.
    ialumnosescnvllgriiimat = models.IntegerField(db_column='iAlumnosEscNvlLgrIIIMat', blank=True, null=True)  # Field name made lowercase.
    ialumnosescnvllgrivmat = models.IntegerField(db_column='iAlumnosEscNvlLgrIVMat', blank=True, null=True)  # Field name made lowercase.
    dporcentalumnsescnvllgrimat = models.FloatField(db_column='dPorcentAlumnsEscNvlLgrIMat', blank=True, null=True)  # Field name made lowercase.
    dporcentalumnsescnvllgriimat = models.FloatField(db_column='dPorcentAlumnsEscNvlLgrIIMat', blank=True, null=True)  # Field name made lowercase.
    dporcentalumnsescnvllgriiimat = models.FloatField(db_column='dPorcentAlumnsEscNvlLgrIIIMat', blank=True, null=True)  # Field name made lowercase.
    dporcentalumnsescnvllgrivmat = models.FloatField(db_column='dPorcentAlumnsEscNvlLgrIVMat', blank=True, null=True)  # Field name made lowercase.
    dporcentalmsescparnvllgrilyc = models.FloatField(db_column='dPorcentAlmsEscParNvlLgrILyC', blank=True, null=True)  # Field name made lowercase.
    dporcentalmsescparnvllgriilyc = models.FloatField(db_column='dPorcentAlmsEscParNvlLgrIILyC', blank=True, null=True)  # Field name made lowercase.
    dporcentalmsescparnvllgriiilyc = models.FloatField(db_column='dPorcentAlmsEscParNvlLgrIIILyC', blank=True, null=True)  # Field name made lowercase.
    dporcentalmsescparnvllgrivlyc = models.FloatField(db_column='dPorcentAlmsEscParNvlLgrIVLyC', blank=True, null=True)  # Field name made lowercase.
    dporcentalmsescparnvllgrimat = models.FloatField(db_column='dPorcentAlmsEscParNvlLgrIMat', blank=True, null=True)  # Field name made lowercase.
    dporcentalmsescparnvllgriimat = models.FloatField(db_column='dPorcentAlmsEscParNvlLgrIIMat', blank=True, null=True)  # Field name made lowercase.
    dporcentalmsescparnvllgriiimat = models.FloatField(db_column='dPorcentAlmsEscParNvlLgrIIIMat', blank=True, null=True)  # Field name made lowercase.
    dporcentalmsescparnvllgrivmat = models.FloatField(db_column='dPorcentAlmsEscParNvlLgrIVMat', blank=True, null=True)  # Field name made lowercase.
    dprctjalmstdsescmxnvllgrilyc = models.FloatField(db_column='dPrctjAlmsTdsEscMxNvlLgrILyC', blank=True, null=True)  # Field name made lowercase.
    dprctjalmstdsescmxnvllgriilyc = models.FloatField(db_column='dPrctjAlmsTdsEscMxNvlLgrIILyC', blank=True, null=True)  # Field name made lowercase.
    dprctjalmstdsescmxnvllgriiilyc = models.FloatField(db_column='dPrctjAlmsTdsEscMxNvlLgrIIILyC', blank=True, null=True)  # Field name made lowercase.
    dprctjalmstdsescmxnvllgrivlyc = models.FloatField(db_column='dPrctjAlmsTdsEscMxNvlLgrIVLyC', blank=True, null=True)  # Field name made lowercase.
    dpctjalmstdsescmxnvllgrimat = models.FloatField(db_column='dPctjAlmsTdsEscMxNvlLgrIMat', blank=True, null=True)  # Field name made lowercase.
    dpctjalmstdsescmxnvllgriimat = models.FloatField(db_column='dPctjAlmsTdsEscMxNvlLgrIIMat', blank=True, null=True)  # Field name made lowercase.
    dpctjalmstdsescmxnvllgriiimat = models.FloatField(db_column='dPctjAlmsTdsEscMxNvlLgrIIIMat', blank=True, null=True)  # Field name made lowercase.
    dpctjalmstdsescmxnvllgrivmat = models.FloatField(db_column='dPctjAlmsTdsEscMxNvlLgrIVMat', blank=True, null=True)  # Field name made lowercase.
    dprctjalmstdsescestnvllgrilyc = models.FloatField(db_column='dPrctjAlmsTdsEscEstNvlLgrILyC', blank=True, null=True)  # Field name made lowercase.
    dprctjalmstdsescestnvllgriilyc = models.FloatField(db_column='dPrctjAlmsTdsEscEstNvlLgrIILyC', blank=True, null=True)  # Field name made lowercase.
    dprctjalmstdsescestnvllgriiilyc = models.FloatField(db_column='dPrctjAlmsTdsEscEstNvlLgrIIILyC', blank=True, null=True)  # Field name made lowercase.
    dprctjalmstdsescestnvllgrivlyc = models.FloatField(db_column='dPrctjAlmsTdsEscEstNvlLgrIVLyC', blank=True, null=True)  # Field name made lowercase.
    dpctjalmstdsescestnvllgrimat = models.FloatField(db_column='dPctjAlmsTdsEscEstNvlLgrIMat', blank=True, null=True)  # Field name made lowercase.
    dpctjalmstdsescestnvllgriimat = models.FloatField(db_column='dPctjAlmsTdsEscEstNvlLgrIIMat', blank=True, null=True)  # Field name made lowercase.
    dpctjalmstdsescestnvllgriiimat = models.FloatField(db_column='dPctjAlmsTdsEscEstNvlLgrIIIMat', blank=True, null=True)  # Field name made lowercase.
    dpctjalmstdsescestnvllgrivmat = models.FloatField(db_column='dPctjAlmsTdsEscEstNvlLgrIVMat', blank=True, null=True)  # Field name made lowercase.
    dsuperaronnvllgrilyc = models.FloatField(db_column='dSuperaronNvlLgrILyC', blank=True, null=True)  # Field name made lowercase.
    dsuperaronnvllgrimat = models.FloatField(db_column='dSuperaronNvlLgrIMat', blank=True, null=True)  # Field name made lowercase.
    dpuntajepromedioescgpocomplyc = models.FloatField(db_column='dPuntajePromedioEscGpoCompLyC', blank=True, null=True)  # Field name made lowercase.
    dpuntajepromedioescgpocompmat = models.FloatField(db_column='dPuntajePromedioEscGpoCompMat', blank=True, null=True)  # Field name made lowercase.
    dpuntajepromediominimogpocomplyc = models.FloatField(db_column='dPuntajePromedioMinimoGpoCompLyC', blank=True, null=True)  # Field name made lowercase.
    dpuntajepromediominimogpocompmat = models.FloatField(db_column='dPuntajePromedioMinimoGpoCompMat', blank=True, null=True)  # Field name made lowercase.
    dpuntajepromediomaximogpocomplyc = models.FloatField(db_column='dPuntajePromedioMaximoGpoCompLyC', blank=True, null=True)  # Field name made lowercase.
    dpuntajepromediomaximogpocompmat = models.FloatField(db_column='dPuntajePromedioMaximoGpoCompMat', blank=True, null=True)  # Field name made lowercase.
    dporcentajeaspecto1lyc = models.FloatField(db_column='dPorcentajeAspecto1LyC', blank=True, null=True)  # Field name made lowercase.
    dporcentajeaspecto2lyc = models.FloatField(db_column='dPorcentajeAspecto2LyC', blank=True, null=True)  # Field name made lowercase.
    dporcentajeaspecto3lyc = models.FloatField(db_column='dPorcentajeAspecto3LyC', blank=True, null=True)  # Field name made lowercase.
    dporcentajeaspecto4lyc = models.FloatField(db_column='dPorcentajeAspecto4LyC', blank=True, null=True)  # Field name made lowercase.
    dporcentajeaspecto1mat = models.FloatField(db_column='dPorcentajeAspecto1Mat', blank=True, null=True)  # Field name made lowercase.
    dporcentajeaspecto2mat = models.FloatField(db_column='dPorcentajeAspecto2Mat', blank=True, null=True)  # Field name made lowercase.
    dporcentajeaspecto3mat = models.FloatField(db_column='dPorcentajeAspecto3Mat', blank=True, null=True)  # Field name made lowercase.
    dporcentajeaspecto4mat = models.FloatField(db_column='dPorcentajeAspecto4Mat', blank=True, null=True)  # Field name made lowercase.
    iindescpresentairregularidad = models.IntegerField(db_column='iIndEscPresentaIrregularidad', blank=True, null=True)  # Field name made lowercase.
    imatriculaprimergrado = models.IntegerField(db_column='iMatriculaPrimerGrado', blank=True, null=True)  # Field name made lowercase.
    imatriculasegundogrado = models.IntegerField(db_column='iMatriculaSegundoGrado', blank=True, null=True)  # Field name made lowercase.
    imatriculatercergrado = models.IntegerField(db_column='iMatriculaTercerGrado', blank=True, null=True)  # Field name made lowercase.
    imatriculacuartogrado = models.IntegerField(db_column='iMatriculaCuartoGrado', blank=True, null=True)  # Field name made lowercase.
    imatriculaquintogrado = models.IntegerField(db_column='iMatriculaQuintoGrado', blank=True, null=True)  # Field name made lowercase.
    imatriculatotal = models.IntegerField(db_column='iMatriculaTotal', blank=True, null=True)  # Field name made lowercase.
    dtasaretencion = models.FloatField(db_column='dTasaRetencion', blank=True, null=True)  # Field name made lowercase.
    dtasamatriculacionoportuna = models.FloatField(db_column='dTasaMatriculacionOportuna', blank=True, null=True)  # Field name made lowercase.
    dporcentajealmnsregularnoextraedad = models.FloatField(db_column='dPorcentajeAlmnsRegularNoExtraEdad', blank=True, null=True)  # Field name made lowercase.
    dtasaaprobacion = models.FloatField(db_column='dTasaAprobacion', blank=True, null=True)  # Field name made lowercase.
    dtasaaprobacionregularizacion = models.FloatField(db_column='dTasaAprobacionRegularizacion', blank=True, null=True)  # Field name made lowercase.
    ifkagrupador = models.IntegerField(db_column='iFkAgrupador', blank=True, null=True)  # Field name made lowercase.
    ifkescuelapromedio = models.IntegerField(db_column='iFkEscuelaPromedio', blank=True, null=True)  # Field name made lowercase.
    dpuntajepromedioestatallyc = models.FloatField(db_column='dPuntajePromedioEstatalLyC', blank=True, null=True)  # Field name made lowercase.
    dpuntajepromedioestatalmat = models.FloatField(db_column='dPuntajePromedioEstatalMat', blank=True, null=True)  # Field name made lowercase.
    ifkcuadranteescuela = models.IntegerField(db_column='iFkCuadranteEscuela', blank=True, null=True)  # Field name made lowercase.) 

    class Meta:
        managed = False
        db_table = 'hechosReporteEmsInee'
        db_tablespace = 'hechos'

class EntidadesFederativas(models.Model):
    ipkentidad_federativa = models.IntegerField(db_column='iPkEntidadFederativa', primary_key=True)  # Field name made lowercase.
    clave_entidad = models.CharField(db_column='cClaveEntidad', max_length=256, blank=True, null=True)  # Field name made lowercase.
    clave_nombre_entidad = models.CharField(db_column='cNombreEntidad', max_length=256, blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'entidadesFederativas'
        db_tablespace = 'dimensionesPlaneaEms'
