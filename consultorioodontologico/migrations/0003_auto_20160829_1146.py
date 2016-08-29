# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorioodontologico', '0002_auto_20160829_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='numero_de_empleado',
            new_name='numero_de_Paciente',
        ),
        migrations.AlterField(
            model_name='horario',
            name='Dias',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.CharField(max_length=200),
        ),
    ]
