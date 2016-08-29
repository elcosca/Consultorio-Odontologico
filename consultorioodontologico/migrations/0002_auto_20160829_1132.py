# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorioodontologico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre_de_la_especialidad', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='horario',
            old_name='Fecha',
            new_name='Dias',
        ),
        migrations.AlterField(
            model_name='medicos',
            name='especialidad',
            field=models.ForeignKey(to='consultorioodontologico.Especialidad'),
        ),
    ]
