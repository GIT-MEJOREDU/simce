#from django.db import models
from django.contrib.gis.db import models

# Create your models here.
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

class Extensionesems(models.Model):
    ipkextensionems = models.IntegerField(db_column='iPkExtensionEms', primary_key=True)  # Field name made lowercase.
    cnombreextensionems = models.CharField(db_column='cNombreExtensionEms', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'extensionesEms'# This is an auto-generated Django model module.

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
