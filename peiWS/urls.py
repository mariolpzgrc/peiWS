from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from pei.views import AreaAcademicaViewSet, AreaFormacionViewSet, EntidadAcademicaViewSet, ExperienciaEductivaViewSet, EvaluadorViewSet, EvaluacionViewSet, PeiViewSet, ParticipanteViewSet, ProgramaEducativoViewSet, RegionViewSet, RolViewSet, UsuarioViewSet

#from pei.views import views
router = DefaultRouter()
router.register(r'areaAcademica', AreaAcademicaViewSet)
router.register(r'areaformacion', AreaFormacionViewSet)
router.register(r'entidadacademica', EntidadAcademicaViewSet)
router.register(r'experienciaeducativa', ExperienciaEductivaViewSet)
router.register(r'evaluador', EvaluadorViewSet, basename="Evaluador")
router.register(r'evaluacion', EvaluacionViewSet)
router.register(r'pei', PeiViewSet)
router.register(r'participante', ParticipanteViewSet)
router.register(r'programaeducativo', ProgramaEducativoViewSet)
router.register(r'rergion', RegionViewSet)
router.register(r'roles', RolViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
