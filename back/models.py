
from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.EmailField(primary_key=True)

    nombre = models.CharField(max_length=30, default='default_value')
    password = models.CharField(max_length=15, default='default_value')
    #dir_entrega = models.CharField(max_length=40, default='default_value')
    #pedidos = models.ForeignKey(Pedido, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)

    nombre_producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre_producto

class Pedido(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    
    id_productos = models.ForeignKey(Producto, on_delete=models.PROTECT)
    #id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    fecha_pedido = models.DateField()
    total = models.IntegerField()
    estado = models.CharField(max_length=15)
    def __int__(self):
        return self.id_pedido