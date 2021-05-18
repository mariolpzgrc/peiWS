from django.db import models
from django.db.models import fields
from django.db.models.fields import files
from rest_framework import serializers
from pei.models import AreaAcademica, AreaFormacion, EntidadAcademica, ExperienciaEducativa, Evaluador, EvaluadorEvaluacion, Evaluacion, Pei, Participante, ProgramaEducativo, ProyectoParticipante, Region, Rol, ParticipanteProgramaEducativo, Usuario


class AreaAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaAcademica
        fields = '__all__'


class AreaFormacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaFormacion
        fields = '__all__'


class EntidadAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntidadAcademica
        fields = '__all__'


class ExperienciaEducativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciaEducativa
        fields = '__all__'


class EvaluadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluador
        fields = '__all__'


class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'


class PeiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pei
        fields = '__all__'


class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__'


class ProgramaEducativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaEducativo
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    idrol = serializers.CharField(read_only=True, source="rol.tiporol")

    class Meta:
        model = Usuario
        fields = '__all__'


class ProyectoParticipanteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProyectoParticipante
        fields = '__all__'

class EvaluadorEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluadorEvaluacion
        fields = '__all__'

class ParticpanteProgramaEducativoSerializer(serializers.Serializer):
    class Meta:
        model = ParticipanteProgramaEducativo
        fields = '__all__'
