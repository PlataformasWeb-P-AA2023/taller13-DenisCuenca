from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'departamentos', views.DepartamentoViewSet)
router.register(r'edificios', views.EdificioViewSet)

urlspatterns = [
    path('api/', include(router.urls)),
]
