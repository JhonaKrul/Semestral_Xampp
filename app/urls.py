from sre_constants import SUCCESS
from django.urls import path
from .views import *


urlpatterns = [
    path('', index , name="Inicio"),
    path('Logeado', indexloged , name="Inicio"),
    path('Carrito/', carrito , name="Carrito"),
    path('Historial/', historial , name="Historial"),
    path('Perfil/', profile , name="Perfil"),
    path('Editar/Perfil/', propiedadesprofile , name="EdicionPerfil"),
    path('Seguimiento/', seguimiento , name="Seguimiento"),
    path('Pagina/', stockpage1nologin , name="Pagina"),
    path('Pagina/', stockpage2 , name="Pagina 2"),
    path('Suscripcion/', suscripcionnologin , name="Suscripcion"),
    path('Suscripcion/', suscripcion , name="Suscripcion"),
    path('Agregar/producto/', agregarproductos, name="Agregarproductos"),
    path('Modificar/producto/<codigo>/', modificar_producto, name="modificar_producto"),
    path('Eliminar_producto/<codigo>/', eliminar_producto, name="eliminar_producto"),
    path('Listar/producto/', listar_productos, name="listar_productos"),
    path('Successful/', successful, name="successful"),
    path('Registro/', registro , name="registro_usuario"),
    path('Login', login, name="login_usuario"),
    path('Pagina/Carrito/', carrito , name="carrito"),
    path('Pagina/Carrito/Carrito/', carrito , name="carrito"),
    path('Carrito/Pagina/', stockpage1nologin , name="pagina"),
    path('Pagina/Carrito/Pagina/', stockpage1nologin , name="pagina"),

]