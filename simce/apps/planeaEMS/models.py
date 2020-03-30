from django.db import models

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
        db_table = 'extensionesEms'