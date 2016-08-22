from django.db import models
from django.utils import timezone


class Paciente (models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    DNI = models.IntegerField()
    direccion_de_correo = models.CharField(max_length=200)
    fecha_de_nacimiento = models.DateTimeField(default=timezone.now)
    numero_de_empleado = models.IntegerField()
    telefono = models.CharField(max_length=200)
    diagnostico = models.CharField(max_length=200)


class Medicos (models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    DNI = models.IntegerField()
    telefono = models.CharField(max_length=200)
    especialidad = models.CharField(max_length=200)
    horarios = models.ForeignKey('Horario')


class Turno (models.Model):
    id_turno = models.IntegerField()
    fecha = models.IntegerField()
    medico = models.ForeignKey('Medicos')
    Paciente = models.ForeignKey('Paciente')


class Horario (models.Model):
    horario_inicio = models.IntegerField()
    horario_fin = models.IntegerField()
    Fecha = models.IntegerField()
