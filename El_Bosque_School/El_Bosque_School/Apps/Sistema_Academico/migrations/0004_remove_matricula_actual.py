# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-03 21:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_Academico', '0003_matricula_actual'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matricula',
            name='Actual',
        ),
    ]
