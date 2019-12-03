from django.conf.urls import url
from El_Bosque_School.Apps.Usuarios.views import *

urlpatterns = [
   url(r'^registrar_usuario',usuario_create.as_view(),name="crear_usuario"),
   url(r'^api_usuarios', UserAPI.as_view(), name="api_usuarios"),
]