# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.db import models

class Facultad (models.Model):
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.Nombre)

    class Meta:

        permissions = (

            ('is_teacher', _('Profesor')),
            ('is_student',_('Estudiante')),
            ('is_major',_('Rector')),
        )

class Carrera (models.Model):
    Nombre = models.CharField(max_length=60)
    Facultad = models.ForeignKey(Facultad, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.Nombre)

class Materia (models.Model):
    Nombre = models.CharField(max_length=50)
    Creditos = models.PositiveSmallIntegerField()
    Facu = models.ForeignKey(Facultad, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.Nombre)

class Estudiante (models.Model):

    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    Nombres = models.CharField(max_length=49)
    Apellidos = models.CharField(max_length=34)
    Identificacion = models.PositiveIntegerField()
    FechaNacimiento = models.DateField()
    LugarNacimiento = models.CharField(max_length=19)
    SEXOS = (('F','Femenino'),('M','Masculino'))
    Sexo= models.CharField(max_length=1, choices=SEXOS,default='M')
    Direccion = models.CharField(max_length=99)
    Telefono = models.PositiveIntegerField()
    Correo = models.CharField(max_length=49)
    Facu = models.ForeignKey(Facultad,null=False, blank=False, on_delete=models.CASCADE)
    Promedio = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    Creditos = models.PositiveSmallIntegerField(default=0)
    CreditosDis = models.PositiveSmallIntegerField(default=0)

    def NombreCompleto (self):
        cadena = "{0} {1}"
        return cadena.format(self.Apellidos, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()

    def calcularPromedio(self):
        e = Estudiante.objects.all()
        tame = len(e)
        i=1

        while (i<=tame):
            matricula = Matricula.objects.all()
            notas = []
            promedio=0
            suma=0

            for matricu in matricula:
                if (matricu.Estudiante.id==i):
                    notas.append(matricu.Nota)

            for nota in notas:
                suma+=nota

            tam = len(notas)

            if(tam==0):
                promedio=0
            else:
                promedio=suma/tam

            estudiante=Estudiante.objects.get(id=i)
            estudiante.Promedio = promedio
            estudiante.save()
            i+=1

        return ' '

    def calcularCreditos (self):
        e = Estudiante.objects.all()
        tam = len(e)
        i =1

        while (i<=tam):
            cred = 0
            prom = Estudiante.objects.get(pk=i).Promedio

            if(prom<3.50):
                cred=10
            else:
                cred=20

            estudiante=Estudiante.objects.get(id=i)
            estudiante.Creditos=cred
            estudiante.save()
            i+=1

        return ' '

    def creditosDisponibles (self):

        est = Estudiante.objects.all()
        e = len(est)
        i=1

        while i <= e :
            estudiantes = Estudiante.objects.get(pk=i)
            creditosac = estudiantes.Creditos
            matricula = Matricula.objects.all()
            mat = []
            credins = 0
            credt = 0

            for m in matricula:
                if (m.Estudiante.id==i):
                    mat.append(m)

            for n in mat:
                credins+=n.Materia.Creditos

            credt = creditosac-credins
            estudiante=Estudiante.objects.get(id=i)
            estudiante.CreditosDis=credt
            estudiante.save()
            i+=1

        return ' '

class Matricula (models.Model):
    Estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    Materia = models.ForeignKey(Materia, null=False, blank=False, on_delete=models.CASCADE)
    FechaMatricula = models.DateTimeField (auto_now_add=True)
    Nota = models.DecimalField(decimal_places=2,max_digits=10,default=0)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Estudiante,self.Materia.Nombre)
