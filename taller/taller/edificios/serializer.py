from django.contrib.auth.models import User, Group
from .models import Edificio, Departamento, Propietario

from rest_framework import serializers


class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Edificio
        fields = "__all__"


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = "__all__"


class PropietarioSerializer(serializers.HyperlinkedModelSerializer):
    departamentos = serializers.SerializerMethodField()
    edificios_nombres = serializers.SerializerMethodField()

    class Meta:
        model = Propietario
        fields = "__all__"

    def get_departamentos(self, obj):
        return obj.obtener_numDeps()

    def get_edificios_nombres(self, obj):
        return obj.edifnombres()
