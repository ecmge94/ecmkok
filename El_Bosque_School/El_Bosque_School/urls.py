"""El_Bosque_School URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from El_Bosque_School.Apps.Sistema_Academico import views
from El_Bosque_School.Apps.Sistema_Academico.views import PDFPrueba

urlpatterns = [
    #url(r'^$',views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^',include ('El_Bosque_School.Apps.Sistema_Academico.urls')),
    url(r'^usuario/', include('El_Bosque_School.Apps.Usuarios.urls')),
    url(r'^login$',login,{'template_name':'index.html'},name='login'),
    url(r'^logout/$',logout_then_login,name='logout'),
    url(r'^mi_pdf/$',PDFPrueba.as_view(),name='mi_pdf'),
]
