from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Departamento, Edificio, Propietario
from .serializer import EdificioSerializer, DepartamentoSerializer, PropietarioSerializer


class EdificioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    # permission_classes = [permissions.IsAuthenticated]


class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PropietarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
    # permission_classes = [permissions.IsAuthenticated]
