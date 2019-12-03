from django import forms
from El_Bosque_School.Apps.Sistema_Academico.models import *

class FacultadForm (forms.ModelForm):

    class Meta:
        model = Facultad

        fields = [

            'Nombre',

        ]

        labels = {

            'Nombre':'Nombre Facultad',
        }

        widgets = {

            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
        }

class CarreraForm (forms.ModelForm):

    class Meta:
        model = Carrera

        fields = [

            'Nombre',
            'Facultad',
        ]

        labels = {

            'Nombre':'Nombre Carrera',
            'Facultad' : 'Facultad Carrera'
        }

        widgets = {

            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
            'Facultad' : forms.Select(attrs={'class':'form-control'}),
        }

class MateriaForm (forms.ModelForm):

    class Meta:

        model = Materia

        fields = [

            'Nombre',
            'Creditos',
            'Facu',
        ]

        labels = {

            'Nombre': 'Nombre Materia',
            'Creditos': 'Creditos',
            'Facu':'Facultad',

        }

        widgets = {

            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Creditos': forms.NumberInput(attrs={'class': 'form-control'}),
            'Facu':forms.Select(attrs={'class': 'form-control'}),
        }

class EstudianteForm (forms.ModelForm):

    class Meta:

        model = Estudiante

        fields = [

            'Usuario',
            'Nombres',
            'Apellidos',
            'Identificacion',
            'FechaNacimiento',
            'LugarNacimiento',
            'Sexo',
            'Direccion',
            'Telefono',
            'Correo',
            'Facu',

        ]

        labels = {

            'Usuario' : 'Usuario Asignado',
            'Nombres' : 'Nombres',
            'Apellidos': 'Apellidos',
            'Identificacion': 'Numero Identificacion',
            'FechaNacimiento': 'Fecha Nacimiento (dd/mm/aaaa)',
            'LugarNacimiento': 'Lugar Nacimiento',
            'Sexo': 'Sexo',
            'Direccion': 'Direccion',
            'Telefono': 'Telefono',
            'Correo': 'Correo',
            'Facu': 'Facultad',

        }

        widgets = {

            'Usuario': forms.Select(attrs={'class':'form-control'}),
            'Nombres': forms.TextInput(attrs={'class':'form-control'}),
            'Apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'Identificacion':forms.NumberInput(attrs={'class':'form-control'}),
            'FechaNacimiento':forms.DateInput(attrs={'class':'form-control'}),
            'LugarNacimiento':forms.TextInput(attrs={'class':'form-control'}),
            'Sexo':forms.Select(attrs={'class':'form-control'}),
            'Direccion':forms.TextInput(attrs={'class':'form-control'}),
            'Telefono':forms.NumberInput(attrs={'class':'form-control'}),
            'Correo':forms.EmailInput(attrs={'class':'form-control'}),
            'Facu':forms.Select(attrs={'class':'form-control'}),
        }

class MatriculaForm(forms.ModelForm):

    class Meta:
        model = Matricula

        fields = [

            'Estudiante',
            'Materia',

        ]

        labels = {

            'Estudiante': 'Estudiante a Matricular',
            'Materia': 'Materia a Matricular',

        }

        widgets = {

            'Estudiante': forms.Select(attrs={'class': 'form-control'}),
            'Materia':forms.Select(attrs={'class': 'form-control'}),

        }

class EstudianteFormOtro (forms.ModelForm):

    class Meta:

        model = Estudiante

        fields = [

            'Nombres',
            'Apellidos',
            'Identificacion',
            'Direccion',
            'Telefono',
            'Facu',

        ]

        labels = {

            'Nombres' : 'Nombres',
            'Apellidos': 'Apellidos',
            'Identificacion': 'Identifiacion',
            'Direccion': 'Direccion',
            'Telefono': 'Telefono',
            'Facu': 'Facultad',

        }

        widgets = {

            'Nombres': forms.TextInput(attrs={'class':'form-control'}),
            'Apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'Identificacion':forms.NumberInput(attrs={'class':'form-control'}),
            'Direccion':forms.TextInput(attrs={'class':'form-control'}),
            'Telefono':forms.NumberInput(attrs={'class':'form-control'}),
            'Facu':forms.Select(attrs={'class':'form-control'}),
        }

class MatriculaFormOtro(forms.ModelForm):

    class Meta:
        model = Matricula

        fields = [

            'Nota',

        ]

        labels = {

            'Nota': 'Nota Materia',

        }

        widgets = {

            'Nota': forms.NumberInput(attrs={'class': 'form-control'}),

        }