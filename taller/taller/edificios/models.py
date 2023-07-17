from django.db import models

from django.db import models


# Create your models here.

class Edificio(models.Model):
    opciones_tipo_Edificio = (
        ('Residencial', 'Residencial'),
        ('Comercial', 'Comercial'),
    )

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, \
                            choices=opciones_tipo_Edificio)

    def _str_(self):
        return "%s %s %s %s" % (self.nombre,
                                self.direccion,
                                self.ciudad,
                                self.tipo)

    def obtener_cuartos(self):
        valor = [t.num_cuartos for t in self.Departamentos.all()]
        valor = sum(valor)
        return valor

    def obtener_costosD(self):
        valor = [t.costo for t in self.Departamentos.all()]
        valor = sum(valor)
        return valor


class Propietario(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cedula = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre

    def edifnombres(self):
        l = (i.edificio.nombre for i in self.departamentos.all())

        # for i in self.departamentos.all():
        #     l += (i.edificio.nombre)

        return set(l)

    def obtener_numDeps(self):
        valor = [t for t in self.departamentos.all()]
        valor = len(valor)
        return valor


class Departamento(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name="departamentos")
    costo = models.FloatField()
    num_cuartos = models.IntegerField()

    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
                                 related_name="Departamentos")

    def _str_(self):
        return "%s %s %d %s" % (self.propietario,
                                self.costo,
                                self.num_cuartos,
                                self.edificio)
