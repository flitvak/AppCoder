from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

# ACA ES DONDE SE GENERAN LAS CLASES

class Curso(models.Model):

    nombre = models.CharField (max_length=40)
    comision = models.IntegerField()

    def __str__(self):
        return f"Curso: {self.nombre} Comisión: {self.comision}" # Esto es para que en el panel de Admin aparezca en texto claro en lugar de que diga Object X

class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=40)
    apeliido = models.CharField (max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} E-mail: {self.email}"

class Profesor(models.Model):
    nombre = models.CharField (max_length=40)
    apellido = models.CharField (max_length=40)
    email = models.EmailField()
    profesion = models.CharField (max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} E-mail: {self.email} Profesión: {self.profesion}"


class Entregable(models.Model):
    nombre = models.CharField (max_length=40)
    fechaDelEntregable = models.DateField()
    entregado = models.BooleanField()   

    def __str__(self):
        return f"Nombre: {self.nombre} Fecha del entregable: {self.fechaDelEntregable} Entregado: {self.entregado}"