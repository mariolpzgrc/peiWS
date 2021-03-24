from django.shortcuts import render
from pei.models import AreaAcademica,  AreaAcademica, AreaFormacion, EntidadAcademica, ExperienciaEducativa, Evaluador, EvaluadorEvaluacion, Evaluacion, Pei, Participante, ProgramaEducativo, ProyectoParticipante, Region, Rol, Usuario
from rest_framework import viewsets
from pei.serializers import AreaAcademicaSerializer, AreaFormacionSerializer, EntidadAcademicaSerializer, ExperienciaEducativaSerializer, EvaluadorSerializer, EvaluacionSerializer, PeiSerializer, ParticipanteSerializer, ProgramaEducativoSerializer, RegionSerializer, RolSerializer, UsuarioSerializer 

class AreaAcademicaViewSet(viewsets.ModelViewSet):
    queryset = AreaAcademica.objects.all()
    serializer_class = AreaAcademicaSerializer

class AreaFormacionViewSet(viewsets.ModelViewSet):
	queryset = AreaFormacion.objects.all()
	serializer_class = AreaFormacionSerializer

class EntidadAcademicaViewSet(viewsets.ModelViewSet):
	queryset = EntidadAcademica.objects.all()
	serializer_class = EntidadAcademicaSerializer

class ExperienciaEductivaViewSet(viewsets.ModelViewSet):
	queryset = ExperienciaEducativa.objects.all()
	serializer_class = ExperienciaEducativaSerializer

class EvaluadorViewSet(viewsets.ModelViewSet):
	queryset = Evaluador.objects.all()
	serializer_class = EvaluadorSerializer

class EvaluacionViewSet(viewsets.ModelViewSet):
	queryset = Evaluacion.objects.all()
	serializer_class = EvaluacionSerializer

class PeiViewSet(viewsets.ModelViewSet):
	queryset = Pei.objects.all()
	serializer_class = PeiSerializer

class ParticipanteViewSet(viewsets.ModelViewSet):
	queryset = Participante.objects.all()
	serializer_class = ParticipanteSerializer

class ProgramaEducativoViewSet(viewsets.ModelViewSet):
	queryset = ProgramaEducativo.objects.all()
	serializer_class = ProgramaEducativoSerializer

class RegionViewSet(viewsets.ModelViewSet):
	queryset  = Region.objects.all()
	serializer_class = RegionSerializer

class RolViewSet(viewsets.ModelViewSet):
	queryset = Rol.objects.all()
	serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer