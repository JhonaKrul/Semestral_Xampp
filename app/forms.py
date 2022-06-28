from unittest.util import _MAX_LENGTH
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#CREAMOS UN TEMPLATE DE UN FORMULARIO

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['codigo','nombre','marca','precio','stock','tipo','imagen','fecha_ingreso']

        nombre = forms.CharField(min_length=10,max_length=20)
        precio = forms.IntegerField(min_value=400)

        widgets = {
            'fecha_ingreso' : forms.SelectDateWidget(years=range(2020,2023))
                }

class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['rut','nombre','apellido','correo','contraseña']

        nombre = forms.CharField(min_length=10,max_length=20)
        rut = forms.CharField(min_length=1)

        widgets = {
            'fecha_ingreso' : forms.SelectDateWidget(years=range(2020,2023))
                }

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']