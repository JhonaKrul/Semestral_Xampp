from pyexpat import model
from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'db_tipo_producto'

class Producto(models.Model):
    codigo = models.IntegerField(null=False,primary_key=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=30)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to="productos", null=True) #agregar campo de imagen
    fecha_ingreso = models.DateField() #Agregar campo de fecha
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    

    class Meta:
        db_table = 'db_producto'

class Usuario(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_usuario'

class Seguimiento(models.Model):
    id_orden = models.IntegerField()
    fecha = models.DateField()
    envio = models.CharField(max_length=40)
    status = models.CharField(max_length=50)
    id_seguimiento = models.CharField(max_length=30)

    def __str__(self):
        return self.id_orden

    class Meta:
        db_table = 'db_seguimiento'

class Historial(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=100)
    modo_pago = models.CharField(max_length=20)
    fecha = models.DateTimeField()
    precio = models.IntegerField()

    def __str__(self):
        return self.codigo

    class Meta:
        db_table = 'db_historial'


    
#Python manage.py makemigrations = crea el script de la base de datos
#Python manage.py migrate = crea la base de datos a partir del script

class Items_carrito(models.Model):
    nombre_producto = models.CharField(max_length=40)
    precio_producto = models.IntegerField()
    imagen = models.ImageField(upload_to="Items_carrito", null=True)

    def __str__(self):
        db_table = "db_items_carrito"

    class Meta:
        db_table = "db_items_carrito"


class carrito(models.Model):
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    class meta:
        db_table = 'db_carrito'
        