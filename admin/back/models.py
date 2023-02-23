
from email.policy import default
from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.EmailField(max_length=150)
    nombre = models.CharField(max_length=30, default='default_value')
    password = models.CharField(max_length=15, default='default_value')
    #dir_entrega = models.CharField(max_length=40, default='default_value') #nullable
    #pedidos = models.ForeignKey(Pedido, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre= models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=True, null=False)
    nombre_producto = models.CharField(max_length=50)
    precio_producto = models.IntegerField()
    stock_producto = models.IntegerField(default='1')
    descripcion_producto = models.CharField(max_length=100)
    imagen = models.CharField(max_length=50, default= 'Sin_imagen')
    #nombre_foto= models.CharField(max_length=256,default='default_value')

    def __str__(self):
        return self.nombre_producto

#class Compra(models.Model):
    #id_productos = models.ForeignKey(Producto, on_delete=models.PROTECT)
    #id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    #fecha_compra = models.DateField()
    #total = models.IntegerField()
    #estado = models.CharField(max_length=15)
    #def __int__(self):
    #    return self.estado

'''
class Detalle_Compra(models.Model):
    
'''

'''
    class Cupon(models.Model):
        id_cupon = models.CharField(max_length=50)
        descripcion = models.CharField(max_length=100)
        categoria_cupon = models.CharField(max_length=50) #todo o categoria especifica
        fecha_inicio = models.DateField(max_length=50) #calculo(sysdate == vencimiento)
        fecha_vencimiento = models.DateField(max_length=50) #calculo(sysdate == vencimiento)
        porc_dscto = int 
        cantidad_usos = total (total-1uso)
        #metodo_pago_permitido

    class Cupones_usados(models.Model):
        id_cupon #fk
        cantidad_descuento_compra = (porc_dscto/100*valor_neto)
        fecha_canje
        correo_usuario #(fk)
'''