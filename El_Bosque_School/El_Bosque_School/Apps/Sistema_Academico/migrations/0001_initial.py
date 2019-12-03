# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-21 04:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombres', models.CharField(max_length=49)),
                ('Apellidos', models.CharField(max_length=34)),
                ('Identificacion', models.PositiveIntegerField()),
                ('FechaNacimiento', models.DateField()),
                ('LugarNacimiento', models.CharField(max_length=19)),
                ('Sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
                ('Direccion', models.CharField(max_length=99)),
                ('Telefono', models.PositiveIntegerField()),
                ('Correo', models.CharField(max_length=49)),
                ('Promedio', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
            ],
            options={
                'permissions': (('is_teacher', 'Profesor'), ('is_student', 'Estudiante'), ('is_major', 'Rector')),
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Creditos', models.PositiveSmallIntegerField()),
                ('Facu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema_Academico.Facultad')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaMatricula', models.DateTimeField(auto_now_add=True)),
                ('Nota', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('Estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema_Academico.Estudiante')),
                ('Materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema_Academico.Materia')),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='Facu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema_Academico.Facultad'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='Usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='carrera',
            name='Facultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema_Academico.Facultad'),
        ),
    ]
