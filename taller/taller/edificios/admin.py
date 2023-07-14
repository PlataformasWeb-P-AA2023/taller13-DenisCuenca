from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Edificio, Departamento


class EdificioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'tipo')


admin.site.register(Edificio, EdificioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombrePropietario', 'costo', 'num_cuartos', 'edificio')
    search_fields = ('nombrePropietario', 'costo')


admin.site.register(Departamento, DepartamentoAdmin)
