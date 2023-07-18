from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from rest_framework import routers
from edificios import views

router = routers.DefaultRouter()
router.register(r'departamentos', views.DepartamentoViewSet)
router.register(r'edificios', views.EdificioViewSet)
router.register(r'propietario', views.PropietarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('edificios.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
