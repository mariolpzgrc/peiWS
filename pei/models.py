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
	idFacultad = models.ForeignKey(Facultad, null=True, blank=True)
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

class Participante(models,Model):
	numeroPersonal = models.CharField(primary_key=True, max_length=10)
	apellidoPaterno = models.TextField(max_length=50)
	apellidoMaterno = models.TextField(max_length=50)
	nombre = models.TextField(max_length=50)
	idAreaAcademica = models.ForeignKey(AreaAcademica, null=False, blank=False)
	idEntidad = models.ForeignKey(Entidad, null=False, blank=False)
	