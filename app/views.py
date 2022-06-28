from django.shortcuts import render,  redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from app.forms import ProductoForm, RegistroUsuarioForm
from .forms import *
from .models import *
import requests 


# Create your views here.

def index(request):
    return render(request, 'app/index.html')

@login_required
def carrito(request):
    carrito = Items_carrito.objects.all()
    datos =  { 'listaCarrito' : carrito }
    
    return render(request, 'app/carrito.html', datos)

def historial(request):
    return render(request, 'app/historial_compra.html')

def login(request):
    return render(request, 'registration/login.html')

def indexloged(request):
    return render(request, 'app/index_loged.html')

def profile(request):
    return render(request, 'app/profile.html')

def propiedadesprofile(request):
    return render(request, 'app/propiedades_perfil.html')

def seguimiento(request):
    return render(request, 'app/seguimiento.html')    

def stockpage1nologin(request):
    response = requests.get('http://127.0.0.1:8000/api/producto/').json()
    response2 = requests.get('https://digimon-api.vercel.app/api/digimon').json()
    response3 = requests.get('https://rickandmortyapi.com/api/character/').json()

    productosAll = Producto.objects.all()
    datos = { 'listaProductos' : productosAll,
              'listaJson' : response,
              'listaDigimon' : response2,
              'listaRM' : response3['results'] }
    
    if request.method == 'POST':

        carrito = Items_carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()

    return render(request, 'app/stock_page_1_sin_login.html', datos)

def stockpage2(request):
    response = requests.get('http://127.0.0.1:8000/api/producto/').json()
    response2 = requests.get('https://digimon-api.vercel.app/api/digimon').json()
    response3 = requests.get('https://rickandmortyapi.com/api/character/').json()

    productosAll = Producto.objects.all()
    datos = { 'listaProductos' : productosAll,
              'listaJson' : response,
              'listaDigimon' : response2,
              'listaRM' : response3['results'] }
    
    if request.method == 'POST':

        carrito = Items_carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()

    return render(request, 'app/stock_page_1_sin_login.html', datos)

def suscripcionnologin(request):
    return render(request, 'app/suscripcion_no_login.html')

def suscripcion(request):
    return render(request, 'app/suscripcion.html')

@permission_required('app.add_producto')
def agregarproductos(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto guardado correctamente!"
    return render(request, 'app/producto/agregar_productos.html', datos)

#SECCION MODIFICAR ( SE TIENE QUE PASAR UN ID )
@permission_required('app.change_producto')
def modificar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,files=request.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto modificado correctamente!"
            datos['form'] = formulario
    return render(request, 'app/producto/modificar_producto.html', datos)

@permission_required('app.view_producto')
def listar_productos(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    
    return render(request, 'app/producto/listar_productos.html', datos)

@permission_required('app.delete_producto')
def eliminar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    
    return redirect(to="listar_productos")


def successful(request):
    carrito = Items_carrito.objects.all()
    carrito.delete()
    
    return render(request, 'app/successful.html')
#Seccion de usuario


def registro(request):
    datos = {
        'form' : RegistroUsuarioForm()
    }
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Usuario guardado correctamente!')
        datos["form"] = formulario

    return render(request, 'registration/registro_usuario.html', datos)