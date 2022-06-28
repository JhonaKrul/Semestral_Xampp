from django.contrib import admin
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','stock','tipo','imagen','fecha_ingreso']
    search_fields = ['codigo']
    list_per_page = 10

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'correo', 'contraseña']
    search_fields = ['rut']
    list_per_page = 10

class ItemAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto']

admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Items_carrito,ItemAdmin)