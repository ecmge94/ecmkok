# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from django.core.urlresolvers import reverse
from El_Bosque_School.Apps.Sistema_Academico.forms import *
from El_Bosque_School.Apps.Sistema_Academico.models import *
from django.views.generic import *
from django.core.urlresolvers import reverse_lazy
from El_Bosque_School.utileria import render_pdf
from django.http import HttpResponse
from El_Bosque_School.Apps.Sistema_Academico.serializers import *
from django.contrib.auth.mixins import PermissionRequiredMixin
import json

# Create your views here.

@login_required
def home(request):
    user = request.user
    if user.has_perm('Sistema_Academico.is_major'):
        return redirect(reverse('home_rector'))
    elif user.has_perm('Sistema_Academico.is_teacher'):
        return redirect(reverse('home_profesor'))
    elif user.has_perm('Sistema_Academico.is_student'):
        return redirect(reverse('home_estudiante'))
    else:
        return render(request, template_name='Sistema_Academico/index.html')

@login_required
@permission_required('Sistema_Academico.is_major')
def home_rector (request):
    return render(request,template_name='Sistema_Academico/index.html')

@login_required
@permission_required('Sistema_Academico.is_teacher')
def home_teacher (request):
    return render(request,template_name='Sistema_Academico/index_profesor.html')

@login_required
@permission_required('Sistema_Academico.is_student')
def home_estudiante (request):
    return render(request,template_name='Sistema_Academico/index_estudiante.html')

@method_decorator(login_required, name='dispatch')
class facultadList (PermissionRequiredMixin, ListView):
    permission_required = 'Sistema_Academico.is_major'
    model = Facultad
    template_name = 'Sistema_Academico/listar_facultad.html'

@method_decorator(login_required, name='dispatch')
class carreraList (ListView):
    model = Carrera
    template_name = 'Sistema_Academico/listar_carrera.html'

@method_decorator(login_required, name='dispatch')
class materiaList (ListView):
    model = Materia
    template_name = 'Sistema_Academico/listar_materia.html'

@method_decorator(login_required, name='dispatch')
class estudianteList (ListView):
    model = Estudiante
    template_name = 'Sistema_Academico/listar_estudiante.html'

@method_decorator(login_required, name='dispatch')
class estudianteListProfesor (ListView):
    model = Estudiante
    template_name = 'Sistema_Academico/listar_estudiante_profesor.html'

@method_decorator(login_required, name='dispatch')
class matriculaList (ListView):
    model = Matricula
    template_name = 'Sistema_Academico/listar_matricula.html'

@method_decorator(login_required, name='dispatch')
class matriculaListEstudiante (ListView):
    model = Matricula
    template_name = 'Sistema_Academico/listar_matricula_estudiante.html'

@method_decorator(login_required, name='dispatch')
class facultadCreate (CreateView):
    model = Facultad
    form_class = FacultadForm
    template_name = 'Sistema_Academico/crear_facultad.html'
    success_url = reverse_lazy('listar_facultad')

@method_decorator(login_required, name='dispatch')
class carreraCreate (CreateView):
    model = Carrera
    form_class = CarreraForm
    template_name = 'Sistema_Academico/crear_carrera.html'
    success_url = reverse_lazy('listar_carrera')

@method_decorator(login_required, name='dispatch')
class materiaCreate (CreateView):
    model = Materia
    form_class = MateriaForm
    template_name = 'Sistema_Academico/crear_materia.html'
    success_url = reverse_lazy('listar_materia')

@method_decorator(login_required, name='dispatch')
class estudianteCreate (CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'Sistema_Academico/crear_estudiante.html'
    success_url = reverse_lazy ('listar_estudiante')

@method_decorator(login_required, name='dispatch')
class matriculaCreate (CreateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'Sistema_Academico/crear_matricula.html'
    success_url = reverse_lazy ('listar_matricula')

@method_decorator(login_required, name='dispatch')
class facultadUpdate (UpdateView):
    model = Facultad
    form_class = FacultadForm
    template_name = 'Sistema_Academico/crear_facultad.html'
    success_url = reverse_lazy ('listar_facultad')

@method_decorator(login_required, name='dispatch')
class carreraUpdate (UpdateView):
    model = Carrera
    form_class = CarreraForm
    template_name = 'Sistema_Academico/crear_carrera.html'
    success_url = reverse_lazy ('listar_carrera')

@method_decorator(login_required, name='dispatch')
class materiaUpdate (UpdateView):
    model = Materia
    form_class = MateriaForm
    template_name = 'Sistema_Academico/crear_materia.html'
    success_url = reverse_lazy ('listar_materia')

@method_decorator(login_required, name='dispatch')
class estudianteUpdate (UpdateView):
    model = Estudiante
    form_class = EstudianteFormOtro
    template_name = 'Sistema_Academico/crear_estudiante.html'
    success_url = reverse_lazy ('listar_estudiante')

@method_decorator(login_required, name='dispatch')
class matriculaUpdate (UpdateView):
    model = Matricula
    form_class = MatriculaFormOtro
    template_name = 'Sistema_Academico/crear_matricula.html'
    success_url = reverse_lazy ('listar_matricula')

@method_decorator(login_required, name='dispatch')
class facultadDelete (DeleteView):
    model = Facultad
    template_name = 'Sistema_Academico/eliminar_facultad.html'
    success_url = reverse_lazy ('listar_facultad')

@method_decorator(login_required, name='dispatch')
class carreraDelete (DeleteView):
    model = Carrera
    template_name = 'Sistema_Academico/eliminar_carrera.html'
    success_url = reverse_lazy ('listar_carrera')

@method_decorator(login_required, name='dispatch')
class materiaDelete (DeleteView):
    model = Materia
    template_name = 'Sistema_Academico/eliminar_materia.html'
    success_url = reverse_lazy ('listar_materia')

@method_decorator(login_required, name='dispatch')
class estudianteDelete (DeleteView):
    model = Estudiante
    template_name = 'Sistema_Academico/eliminar_estudiante.html'
    success_url = reverse_lazy ('listar_estudiante')

@method_decorator(login_required, name='dispatch')
class matriculaDelete (DeleteView):
    model = Matricula
    template_name = 'Sistema_Academico/eliminar_matricula.html'
    success_url = reverse_lazy ('listar_matricula')

@method_decorator(login_required, name='dispatch')
class buscarView (TemplateView):

 def post(self,request,*args,**kwargs):
    buscar = request.POST['buscalo']
    estudiantes = Estudiante.objects.filter(Facu__Nombre__contains=buscar)
    matriculas = Matricula.objects.filter(Materia__Nombre__contains=buscar)
    if matriculas:
        return render(request,'Sistema_Academico/buscar.html',{'matriculas':matriculas,'matricula':True})
    elif estudiantes:
        return render(request, 'Sistema_Academico/buscar.html',{'estudiantes':estudiantes,'estudiante':True})
    else:
        estudiantes = Estudiante.objects.filter(Identificacion__exact=buscar)
        return render(request, 'Sistema_Academico/buscar.html',{'estudiantes':estudiantes,'estudiante':True})

@method_decorator(login_required, name='dispatch')
class PDFPrueba(View):

    def get (self,request,*args,**kwargs):
        pdf = render_pdf("Sistema_Academico/buscar.html")
        return HttpResponse (pdf,content_type="application/pdf")

class estudianteAPI(APIView):

    serializer=estudianteSerializer

    def get(self,request, format=None):
        lista = Estudiante.objects.all()
        response= self.serializer(lista,many=True)

        return HttpResponse (json.dumps(response.data),content_type='application/json')

