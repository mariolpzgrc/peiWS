from django.contrib import admin
from .models import AreaAcademica, AreaFormacion, EntidadAcademica, ExperienciaEducativa, Evaluador, EvaluadorEvaluacion, Evaluacion, Pei, Participante, ProgramaEducativo, ProyectoParticipante, Region, Rol,Usuario

# Register your models here.
admin.site.register(AreaAcademica)
admin.site.register(AreaFormacion)
admin.site.register(EntidadAcademica)
admin.site.register(ExperienciaEducativa)
admin.site.register(Evaluador)
admin.site.register(EvaluadorEvaluacion)
admin.site.register(Evaluacion)
admin.site.register(Pei)
admin.site.register(Participante)
admin.site.register(ProgramaEducativo)
admin.site.register(ProyectoParticipante)
admin.site.register(Region)
admin.site.register(Rol)
admin.site.register(Usuario)