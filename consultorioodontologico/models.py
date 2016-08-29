from django.db import models
from django.utils import timezone


class Paciente (models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    DNI = models.IntegerField()
    direccion_de_correo = models.CharField(max_length=200)
    fecha_de_nacimiento = models.DateTimeField(default=timezone.now)
    numero_de_Paciente = models.IntegerField()
    telefono = models.CharField(max_length=200)
    diagnostico = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Medicos (models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    DNI = models.IntegerField()
    telefono = models.CharField(max_length=200)
    especialidad = models.ForeignKey('Especialidad')
    horarios = models.ForeignKey('Horario')

    def __str__(self):
        return self.nombre


class Turno (models.Model):
    id_turno = models.IntegerField()
    fecha = models.CharField(max_length=200)
    medico = models.ForeignKey('Medicos')
    Paciente = models.ForeignKey('Paciente')

    def __str__(self):
        return self.fecha


class Horario (models.Model):
    horario_inicio = models.CharField(max_length=200)
    horario_fin = models.CharField(max_length=200)
    Dias = models.CharField(max_length=200)

    def __str__(self):
        return self.Dias


class Especialidad (models.Model):
    nombre_de_la_especialidad = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_de_la_especialidad