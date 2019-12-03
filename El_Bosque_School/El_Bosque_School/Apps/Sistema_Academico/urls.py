from django.conf.urls import url
from El_Bosque_School.Apps.Sistema_Academico.views import *

urlpatterns = [

    url(r'^$', home, name='home'),
    url(r'^home_rector/$', home_rector, name='home_rector'),
    url(r'^home_profesor/$', home_teacher , name='home_profesor'),
    url(r'^home_estudiante/$', home_estudiante, name='home_estudiante'),
    url(r'^facultad_creacion$',facultadCreate.as_view(),name='crear_facultad'),
    url(r'^carrera_creacion$',carreraCreate.as_view(),name='crear_carrera'),
    url(r'^materia_creacion$',materiaCreate.as_view(),name='crear_materia'),
    url(r'^estudiante_creacion$',estudianteCreate.as_view(), name='crear_estudiante'),
    url(r'^matricula_creacion$',matriculaCreate.as_view(), name='crear_matricula'),
    url(r'^facultad_listar$', facultadList.as_view(), name='listar_facultad'),
    url(r'^carrera_listar$', carreraList.as_view(), name='listar_carrera'),
    url(r'^materia_listar$', materiaList.as_view(), name='listar_materia'),
    url(r'^estudiante_listar$', estudianteList.as_view(), name='listar_estudiante'),
    url(r'^estudiante_listar_profe$', estudianteListProfesor.as_view(), name='listar_estudiante_profe'),
    url(r'^matricula_listar$', matriculaList.as_view(), name='listar_matricula'),
    url(r'^matricula_listar_estudiante$', matriculaListEstudiante.as_view(), name='listar_matricula_estudiante'),
    url(r'^facultad_editar/(?P<pk>\d+)/$', facultadUpdate.as_view(), name='editar_facultad'),
    url(r'^carrera_editar/(?P<pk>\d+)/$', carreraUpdate.as_view(), name='editar_carrera'),
    url(r'^materia_editar/(?P<pk>\d+)/$', materiaUpdate.as_view(), name='editar_materia'),
    url(r'^estudiante_editar/(?P<pk>\d+)/$', estudianteUpdate.as_view(), name='editar_estudiante'),
    url(r'^matricula_editar/(?P<pk>\d+)/$',matriculaUpdate.as_view() , name='editar_matricula'),
    url(r'^facultad_eliminar/(?P<pk>\d+)/$', facultadDelete.as_view() , name='eliminar_facultad'),
    url(r'^carrera_eliminar/(?P<pk>\d+)/$', carreraDelete.as_view(), name='eliminar_carrera'),
    url(r'^materia_eliminar/(?P<pk>\d+)/$', materiaDelete.as_view(), name='eliminar_materia'),
    url(r'^estudiante_eliminar/(?P<pk>\d+)/$', estudianteDelete.as_view(), name='eliminar_estudiante'),
    url(r'^matricula_eliminar/(?P<pk>\d+)/$', matriculaDelete.as_view(), name='eliminar_matricula'),
    url(r'^buscar$', buscarView.as_view(), name='buscar'),
    url(r'^api_estudiantes', estudianteAPI.as_view(), name="api_estudiantes"),

]