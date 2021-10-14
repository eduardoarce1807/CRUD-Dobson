from django.db import models

# Create your models here.

class Genero(models.Model):
    IdGenero = models.AutoField(primary_key=True)
    NombreGenero = models.CharField(max_length=250)
    EstadoGenero = models.IntegerField()

class Especie(models.Model):
    IdEspecie = models.AutoField(primary_key=True)
    NombreEspecie = models.CharField(max_length=250)
    EstadoEspecie = models.IntegerField()

class FamiliaDeOrquideas(models.Model):
    IdFamiliaDeOrquideas = models.AutoField(primary_key=True)
    NombreFamiliaDeOrquideas = models.CharField(max_length=250)
    EstadoFamiliaDeOrquideas = models.IntegerField()
