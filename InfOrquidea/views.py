from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from InfOrquidea.models import Genero,Especie,FamiliaDeOrquideas
from InfOrquidea.serializers import GeneroSerializer,EspecieSerializer,FamiliaDeOrquideasSerializer


# Create your views here.

#GENERO
@csrf_exempt
def generoApi(request,id=0):
    if request.method=='GET':
        generos = Genero.objects.all()
        generos_serializer=GeneroSerializer(generos,many=True)
        return JsonResponse(generos_serializer.data,safe=False)

    elif request.method=='POST':
        genero_data=JSONParser().parse(request)
        generos_serializer=GeneroSerializer(data=genero_data)
        if generos_serializer.is_valid():
            generos_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        genero_data=JSONParser().parse(request)
        genero=Genero.objects.get(IdGenero=genero_data['IdGenero'])
        generos_serializer=GeneroSerializer(genero,data=genero_data)
        if generos_serializer.is_valid():
            generos_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        genero=Genero.objects.get(IdGenero=id)
        genero.delete()
        return JsonResponse("Deleted Successfully",safe=False)

#ESPECIE
@csrf_exempt
def especieApi(request,id=0):
    if request.method=='GET':
        especies = Especie.objects.all()
        especies_serializer=EspecieSerializer(especies,many=True)
        return JsonResponse(especies_serializer.data,safe=False)

    elif request.method=='POST':
        especie_data=JSONParser().parse(request)
        especies_serializer=EspecieSerializer(data=especie_data)
        if especies_serializer.is_valid():
            especies_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        especie_data=JSONParser().parse(request)
        especie=Especie.objects.get(IdEspecie=especie_data['IdEspecie'])
        especies_serializer=EspecieSerializer(especie,data=especie_data)
        if especies_serializer.is_valid():
            especies_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        especie=Especie.objects.get(IdEspecie=id)
        especie.delete()
        return JsonResponse("Deleted Successfully",safe=False)

#FAMILIADEORQUIDEAS
@csrf_exempt
def familiaDeOrquideaApi(request,id=0):
    if request.method=='GET':
        FamiliaDeOrquidea = FamiliaDeOrquideas.objects.all()
        FamiliaDeOrquideas_serializer=FamiliaDeOrquideasSerializer(FamiliaDeOrquidea,many=True)
        return JsonResponse(FamiliaDeOrquideas_serializer.data,safe=False)

    elif request.method=='POST':
        FamiliaDeOrquidea_data=JSONParser().parse(request)
        FamiliaDeOrquideas_serializer=FamiliaDeOrquideasSerializer(data=FamiliaDeOrquidea_data)
        if FamiliaDeOrquideas_serializer.is_valid():
            FamiliaDeOrquideas_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        FamiliaDeOrquidea_data=JSONParser().parse(request)
        FamiliaDeOrquidea=FamiliaDeOrquideas.objects.get(IdFamiliaDeOrquideas=FamiliaDeOrquidea_data['IdFamiliaDeOrquideas'])
        FamiliaDeOrquideas_serializer=FamiliaDeOrquideasSerializer(FamiliaDeOrquidea,data=FamiliaDeOrquidea_data)
        if FamiliaDeOrquideas_serializer.is_valid():
            FamiliaDeOrquideas_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        FamiliaDeOrquidea=FamiliaDeOrquideas.objects.get(IdFamiliaDeOrquideas=id)
        FamiliaDeOrquidea.delete()
        return JsonResponse("Deleted Successfully",safe=False)

