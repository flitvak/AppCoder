from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

# ACA ES DONDE SE GENERAN LAS CLASES

class Curso(models.Model):

    nombre = models.CharField (max_length=40)
    comision = models.IntegerField()

class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=40)
    apeliido = models.CharField (max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField (max_length=40)
    apellido = models.CharField (max_length=40)
    email = models.EmailField()
    profesion = models.CharField (max_length=40)

class Entregable(models.Model):
    nombre = models.CharField (max_length=40)
    fechaDelEntregable = models.DateField()
    entregado = models.BooleanField()   