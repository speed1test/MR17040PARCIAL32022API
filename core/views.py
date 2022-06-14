from django.shortcuts import render
from core.serializers import ConductorSerializer, VehiculoSerializer
from rest_framework import viewsets, permissions
from core.models import *
# Create your views here.
class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer
    permissions = [permissions.AllowAny]
 

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permissions = [permissions.AllowAny]
 