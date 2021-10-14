from rest_framework import serializers
from InfOrquidea.models import Genero,Especie,FamiliaDeOrquideas

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genero
        fields=('IdGenero','NombreGenero','EstadoGenero')

class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Especie
        fields=('IdEspecie','NombreEspecie','EstadoEspecie')

class FamiliaDeOrquideasSerializer(serializers.ModelSerializer):
    class Meta:
        model=FamiliaDeOrquideas
        fields=('IdFamiliaDeOrquideas','NombreFamiliaDeOrquideas','EstadoFamiliaDeOrquideas')