from django.urls import path, include
from rest_framework import routers
from .views import * 

#se encarga de darle ruta al api
router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

]