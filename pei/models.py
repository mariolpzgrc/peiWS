from django.db import models

# Create your models here.
class Usuario (models.Model):
	numeroPersonal = models.AutoField(primary_key=True)
	nombre = models.TextField(max_length=50)
	apellidoPaterno = models.TextField(max_length=50)
	apellidoMaterno = models.TextField(max_length=50)
	telefono = models.CharField(max_length=10)
	extension = models.CharField(max_length=5)
	celular = models.CharField(max_length=10)
	correo = models.EmailField(max_length=50)
	idFacultad = models.ForeignKey(Entidad, null=True, blank=True)
	idPei = models.ForeignKey(Pei, null=True, blank=True)
	contrasena = models.CharField(max_length=50)
	fechaCreacion = models.DateTimeField(auto_now_add=True)
	fechaActualizacion = models.DateTimeField(auto_now=True)

	def __str__(self):
		return Usuario

class Pei(models.Model):
	numeroPei = models.AutoField(primary_key=True)
	nombrePei = models.TextField(max_length=100)
	descripcionPei = models.TextField(max_length=300)
	fechaIncicio = models.DateTimeField()
	fechaTermino = models.DateTimeField()
	numeroParticipantesPei = models.IntegerField(max_length=3)
	fechaCreacion = models.DateTimeField(auto_now_add=True)
	fechaActualizacion = models.DateTimeField(auto_now=True)


	def __str__(self):
		return Pei

class Participante(models,Model):
	numeroPersonal = models.CharField(primary_key=True, max_length=10)
	apellidoPaterno = models.TextField(max_length=50)
	apellidoMaterno = models.TextField(max_length=50)
	nombre = models.TextField(max_length=50)
	idAreaAcademica = models.ForeignKey(AreaAcademica, null=False, blank=False)
	idEntidad = models.ForeignKey(Entidad, null=False, blank=False)
	idProgramaEducativo = models.ForeignKey(ProgramaEducativo, null=False, blank=False)
	idExperienciasEducativas = models.ForeignKey(ExperienciasEducativa, null=False, blank=False)
	idAreaFormacion = models.ForeignKey(AreaFormacion, null=False, blank=False)
	idRegion = models.ForeignKey(Region, null=False, blank=False)

		def __str__(self):
			return Participante


class Entidad(models.Model):
	idEntidad = models.AutoField(primary_key=True)
	nombreEntidad = models.TextField(max_length=100)

	def __str__(self):
		return Entidad

class ProgramaEducativo(models.Model)
	idProgramaEducativo = models.AutoField(primary_key=True)
	nombreProgramaEducativo = models.TextField(max_length=100)

	def __str__(self):
		return ProgramaEducativo

class ExperienciaEducativa(models.Model):
	idExperienciasEducativa = models.AutoField(primary_key=True)
	nombreExperienciaEducativa = models.TextField(max_length=50)

	def __str__(self):
		return ExperienciaEducativa