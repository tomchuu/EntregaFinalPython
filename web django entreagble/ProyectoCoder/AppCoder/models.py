from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gimnasio(models.Model):
    
    nombre = models.CharField(max_length=60)
    valoracion = models.IntegerField()



class Cliente(models.Model):

    def __str__(self):
        return f"Cliente {self.nombre} {self.apellido} , Ingresado en la fecha y horario de : {self.fechadeingreso}"

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    fechadeingreso = models.DateTimeField()



class Rutinas(models.Model):

    def __str__(self):
        return f"Tipo de rutina {self.nombre} , Dias y horas de la rutina {self.dias}"

    nombre = models.CharField(max_length=60)
    dias = models.DateTimeField()


class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)