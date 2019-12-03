# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import *
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from El_Bosque_School.Apps.Sistema_Academico.models import *
from django.views.generic import *
from django.core.urlresolvers import reverse_lazy
from El_Bosque_School.Apps.Usuarios.forms import UserForm
from rest_framework.views import APIView
from El_Bosque_School.Apps.Usuarios.serializers import UsersSerializer
import json

@method_decorator(login_required,name='dispatch')
class usuario_create (CreateView):
    model = User
    template_name = 'Usuarios/crear_usuarios.html'
    form_class = UserForm
    success_url = reverse_lazy('home')

class UserAPI(APIView):
    serializer=UsersSerializer

    def get(self,request, format=None):
        lista = User.objects.all()
        response= self.serializer(lista,many=True)

        return HttpResponse (json.dumps(response.data),content_type='application/json')
