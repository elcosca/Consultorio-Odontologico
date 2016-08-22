# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('horario_inicio', models.IntegerField()),
                ('horario_fin', models.IntegerField()),
                ('Fecha', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('DNI', models.IntegerField()),
                ('telefono', models.CharField(max_length=200)),
                ('especialidad', models.CharField(max_length=200)),
                ('horarios', models.ForeignKey(to='consultorioodontologico.Horario')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('DNI', models.IntegerField()),
                ('direccion_de_correo', models.CharField(max_length=200)),
                ('fecha_de_nacimiento', models.DateTimeField(default=django.utils.timezone.now)),
                ('numero_de_empleado', models.IntegerField()),
                ('telefono', models.CharField(max_length=200)),
                ('diagnostico', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('id_turno', models.IntegerField()),
                ('fecha', models.IntegerField()),
                ('Paciente', models.ForeignKey(to='consultorioodontologico.Paciente')),
                ('medico', models.ForeignKey(to='consultorioodontologico.Medicos')),
            ],
        ),
    ]
