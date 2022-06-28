from django.shortcuts import render
from rest_framework import viewsets
from app.models import * 
from .serializers import *

# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer