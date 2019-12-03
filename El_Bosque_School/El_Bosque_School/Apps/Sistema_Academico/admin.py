# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from El_Bosque_School.Apps.Sistema_Academico.models import *

# Register your models here.

admin.site.register(Facultad)
admin.site.register(Materia)
admin.site.register(Estudiante)
admin.site.register(Matricula)
admin.site.register(Carrera)