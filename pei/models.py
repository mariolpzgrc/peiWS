# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from typing import Pattern
from django import db
from django.db import models


class AreaAcademica(models.Model):
    # Field name made lowercase.
    idareaacademica = models.BigAutoField(
        db_column='idAreaAcademica', primary_key=True)
    # Field name made lowercase.
    nombreareaacademica = models.CharField(
        db_column='nombreAreaAcademica', max_length=100)

    class Meta:
        managed = False
        db_table = "area_academica"

    def __Str__(self):
        return self.nombreareaacademica


class AreaFormacion(models.Model):
    # Field name made lowercase.
    idareaformacion = models.BigAutoField(
        db_column='idAreaFormacion', primary_key=True)
    # Field name made lowercase.
    nombreareaformacion = models.CharField(
        db_column='nombreAreaFormacion', max_length=100)

    class Meta:
        managed = False
        db_table = 'area_formacion'

    def __str__(self):
        return self.nombreareaformacion


class EntidadAcademica(models.Model):
    # Field name made lowercase.
    identidadacademica = models.BigAutoField(
        db_column='idEntidadAcademica', primary_key=True)
    # Field name made lowercase.
    nombreentidadacademica = models.CharField(
        db_column='nombreEntidadAcademica', max_length=100)

    class Meta:
        managed = False
        db_table = 'entidad_academica'

    def __str__(self):
        return self.nombreentidadacademica


class Evaluador(models.Model):
    # Field name made lowercase.
    numeropersonal = models.IntegerField(
        db_column='numeroPersonal', primary_key=True)
    nombre = models.CharField(max_length=50)
    # Field name made lowercase.
    apellidopaterno = models.CharField(
        db_column='apellidoPaterno', max_length=50)
    # Field name made lowercase.
    apellidomaterno = models.CharField(
        db_column='apellidoMaterno', max_length=50)
    # Field name made lowercase.
    fechainicio = models.DateField(db_column='fechaInicio')
    # Field name made lowercase.
    fechatermino = models.DateField(db_column='fechaTermino')
    # Field name made lowercase.
    idcomision = models.IntegerField(db_column='idComision')
    firma = models.ImageField(upload_to="firma", null=True)
    password = models.CharField(max_length=20)
    # Field name made lowercase.
    idrol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='idRol')

    class Meta:
        managed = False
        db_table = 'evaluador'

    def __str__(self):
        return self.nombre + ' ' + self.apellidopaterno + ' ' + self.apellidomaterno


class EvaluadorEvaluacion(models.Model):
    # Field name made lowercase.
    idevaluador_pei = models.BigAutoField(
        db_column='idEvaluador_PEI', primary_key=True)
    # Field name made lowercase.
    idevaluacion = models.ForeignKey(
        'Evaluacion', models.DO_NOTHING, db_column='idEvaluacion')
    # Field name made lowercase.
    idevaluador = models.ForeignKey(
        Evaluador, models.DO_NOTHING, db_column='idEvaluador')

    class Meta:
        managed = False
        db_table = 'evaluador_evaluacion'


class Evaluacion(models.Model):
    # Field name made lowercase.
    folioevaluacion = models.BigAutoField(
        db_column='folioEvaluacion', primary_key=True)
    # Field name made lowercase.
    idpei = models.ForeignKey('Pei', models.DO_NOTHING, db_column='idPEI')
    observaciones = models.TextField()
    # Field name made lowercase.
    puntajesuficiencia = models.IntegerField(db_column='puntajeSuficiencia')
    # Field name made lowercase.
    puntajefinal = models.IntegerField(db_column='puntajeFinal')
    # Field name made lowercase.
    puntajeconguencia = models.IntegerField(
        db_column='puntajeConguencia', blank=True, null=True)
    # Field name made lowercase.
    puntajeimpacto = models.IntegerField(
        db_column='puntajeImpacto', blank=True, null=True)
    # Field name made lowercase.
    puntajepertinencia = models.IntegerField(
        db_column='puntajePertinencia', blank=True, null=True)
    horaInicio = models.DateTimeField(db_column='horaInicio', blank=True)
    horaFinal = models.DateTimeField(db_column='horaFinal', blank=True)
    diaEvaluacion = models.CharField(
        db_column='diaEvaluacion', blank=True, max_length=15)

    class Meta:
        managed = False
        db_table = 'evaluacion'

    def __str__(self):
        return self.folioevaluacion


class ExperienciaEducativa(models.Model):
    # Field name made lowercase.
    idexperienciaeducativa = models.BigAutoField(
        db_column='idExperienciaEducativa', primary_key=True)
    # Field name made lowercase.
    nombreexperinciaeducativa = models.CharField(
        db_column='nombreExperinciaEducativa', max_length=100)
    # Field name made lowercase.
    idprogramaeducativo = models.ForeignKey(
        'ProgramaEducativo', models.DO_NOTHING, db_column='idProgramaEducativo')

    class Meta:
        managed = False
        db_table = 'experiencia_educativa'

    def __str__(self):
        return self.nombreexperienciaeducativa


class Participante(models.Model):
    # Field name made lowercase.
    numeroconsecutivo = models.BigAutoField(
        db_column='numeroConsecutivo', primary_key=True)
    # Field name made lowercase.
    numeropersonal = models.CharField(
        db_column='numeroPersonal', max_length=20)
    nombre = models.CharField(max_length=50)
    # Field name made lowercase.
    apellidopaterno = models.CharField(
        db_column='apellidoPaterno', max_length=50)
    # Field name made lowercase.
    apellidomaterno = models.CharField(
        db_column='apellidoMaterno', max_length=50)
    # Field name made lowercase.
    idprogramaeducativo = models.ForeignKey(
        'ProgramaEducativo', models.DO_NOTHING, db_column='idProgramaEducativo')
    # Field name made lowercase.
    idexperienciaeducativa = models.ForeignKey(
        ExperienciaEducativa, models.DO_NOTHING, db_column='idExperienciaEducativa')
    # Field name made lowercase.
    identidad = models.ForeignKey(
        EntidadAcademica, models.DO_NOTHING, db_column='idEntidad')
    password = models.CharField(max_length=20)
    # Field name made lowercase.
    idareaacademica = models.ForeignKey(
        AreaAcademica, models.DO_NOTHING, db_column='idAreaAcademica')
    # Field name made lowercase.
    idregion = models.ForeignKey(
        'Region', models.DO_NOTHING, db_column='idRegion')
    # Field name made lowercase.
    idrol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='idRol')
    # Field name made lowercase.
    idareaformacion = models.ForeignKey(
        AreaFormacion, models.DO_NOTHING, db_column='idAreaFormacion')

    class Meta:
        managed = False
        db_table = 'participante'

    def __str__(self):
        return self.nombre + ' ' + self.apellidopaterno + ' ' + self.apellidomaterno


class Pei(models.Model):
    folio = models.BigAutoField(primary_key=True)
    # Field name made lowercase.
    nombreproyecto = models.CharField(
        db_column='nombreProyecto', max_length=100, blank=True, null=False)
    descripcion = models.TextField()
    # Field name made lowercase.
    fechainicio = models.DateField(
        db_column='fechaInicio', blank=True, null=True)
    # Field name made lowercase.
    fechatermino = models.DateField(
        db_column='fechaTermino', blank=True, null=True)
    ambitoAplicacion = models.TextField(
        db_column='ambitoAplicacion', blank=True, max_length=500)
    incorporarRua = models.BooleanField(db_column='incorporarRua')
    urlDocumentacion = models.CharField(
        db_column='urlDocumentacion', max_length=255, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'pei'

    def __str__(self):
        return self.nombreproyecto

class PeiEvaluado(models.Model):
    # Field name made lowercase.
    id = models.BigAutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    idevaluador = models.ForeignKey(
        Evaluador, models.DO_NOTHING, db_column='idEvaluador')
    # Field name made lowercase.
    idproyecto = models.ForeignKey(
        Pei, models.DO_NOTHING, db_column='idProyecto')
    # Field name made lowercase.
    idevaluacion = models.ForeignKey(
        Evaluacion, models.DO_NOTHING, db_column='idEvaluacion')

    class Meta:
        managed = False
        db_table = 'pei_evaluado'


class ProgramaEducativo(models.Model):
    # Field name made lowercase.
    idprogramaeducativo = models.BigAutoField(
        db_column='idProgramaEducativo', primary_key=True)
    # Field name made lowercase.
    nombreprogramaeducativo = models.CharField(
        db_column='nombreProgramaEducativo', max_length=100)
    # Field name made lowercase.
    identidadacademica = models.ForeignKey(
        EntidadAcademica, models.DO_NOTHING, db_column='idEntidadAcademica')
    # Field name made lowercase.
    idregion = models.ForeignKey(
        'Region', models.DO_NOTHING, db_column='idRegion')

    class Meta:
        managed = False
        db_table = 'programa_educativo'


class ProyectoParticipante(models.Model):
    # Field name made lowercase.
    id = models.BigAutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    idparticipante = models.ForeignKey(
        Participante, models.DO_NOTHING, db_column='idParticipante')
    # Field name made lowercase.
    idproyecto = models.ForeignKey(
        Pei, models.DO_NOTHING, db_column='idProyecto')

    class Meta:
        managed = False
        db_table = 'proyecto_participante'


class Region(models.Model):
    # Field name made lowercase.
    idregion = models.BigAutoField(db_column='idRegion', primary_key=True)
    # Field name made lowercase.
    nombreregion = models.CharField(db_column='nombreRegion', max_length=100)

    class Meta:
        managed = False
        db_table = 'region'

    def __str__(self):
        return self.nombreregion


class Rol(models.Model):
    # Field name made lowercase.
    idrol = models.BigAutoField(db_column='idRol', primary_key=True)
    # Field name made lowercase.
    tiporol = models.CharField(db_column='tipoRol', max_length=20)

    class Meta:
        managed = False
        db_table = 'rol'

    def __str__(self):
        return self.tiporol


class ParticipanteProgramaEducativo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    idParticipante = models.ForeignKey(
        Participante, models.DO_NOTHING, db_column='idParticipante')
    idProgramaEducativo = models.ForeignKey(
        ProgramaEducativo, models.DO_NOTHING, db_column='idProgramaEducativo')

    class Meta:
        managed = False
        db_table = 'participante_programaeducativo'


class Usuario(models.Model):
    # Field name made lowercase.
    numeropersonal = models.CharField(
        db_column='numeroPersonal', primary_key=True, max_length=20)
    nombre = models.CharField(max_length=50)
    # Field name made lowercase.
    apellidopaterno = models.CharField(
        db_column='apellidoPaterno', max_length=50)
    # Field name made lowercase.
    apellidomaterno = models.CharField(
        db_column='apellidoMaterno', max_length=50)
    # Field name made lowercase.
    idprogramaeducativo = models.IntegerField(
        db_column='idProgramaEducativo', blank=True, null=True)
    # Field name made lowercase.
    idexperienciaeducativa = models.IntegerField(
        db_column='idExperienciaEducativa', blank=True, null=True)
    # Field name made lowercase.
    identidad = models.IntegerField(
        db_column='idEntidad', blank=True, null=True)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=20)
    # Field name made lowercase.
    idrol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='idRol')

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return self.nombre + ' ' + self.apellidopaterno + ' ' + self.apellidomaterno
