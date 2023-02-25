from email.policy import default
from django.db import models
from datetime import datetime
from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm
# Create your models here.
# mirando que campos se pueden validar con validators

class Usuario(models.Model):
    email = models.EmailField(max_length=150)
    nombre = models.CharField(max_length=30, default='Nombre usuario')
    password = models.CharField(max_length=15, default='password usuario')
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

    class Meta:
        verbose_name='Producto old'
        verbose_name_plural='Producto old'
        ordering=['categoria']


    def __str__(self):
        return self.nombre_producto
    
#Update Base Datos--------------------------------------------------------------------------------

class cliente(models.Model):
    cli_email = models.EmailField(primary_key=True, default='Email cliente', max_length=30,verbose_name='Email cliente', validators=[validators.EmailValidator(message="Correo electrónico inválido")])
    cli_password = models.CharField(max_length=32, default='Contraseña cliente', verbose_name='Contraseña')
    cli_nombre = models.CharField(max_length=30, default='Nombre cliente', verbose_name='Nombre cliente')
    cli_apellido = models.CharField(max_length=30, default='Apellido cliente', verbose_name='Apellido cliente')
    cli_direccion_entrega = models.CharField(max_length=40, default='Dirección sin definir', verbose_name='Dirección entrega cliente')
    cli_donador = models.BooleanField(default=False,verbose_name='Donador')

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
        ordering=['cli_email']

    def __str__(self):
        return self.cli_email

class personal_tienda(models.Model):
    per_email = models.EmailField(primary_key=True,default='Email empleado', max_length=30,verbose_name='Email empleado', validators=[validators.EmailValidator(message="Correo electrónico inválido")])
    per_password = models.CharField(max_length=32,default='Contraseña empleado', null=False, blank=False, verbose_name='Contraseña')
    per_nombre = models.CharField(max_length=30, default='Nombre empleado', verbose_name='Nombre empleado')
    per_apellido = models.CharField(max_length=30, default='Apellido empleado', verbose_name='Apellido empleado')
    per_ciudad_residencia = models.CharField(max_length=40, default='Ciudad sin definir', verbose_name='Ciudad de residencia')
    per_comuna_residencia = models.CharField(max_length=40, default='Comuna sin definir', verbose_name='Comuna de residencia')
    per_run = models.IntegerField(blank=False, null=False, verbose_name='Run personal')
    per_dvrun = models.CharField(max_length=1 ,blank=False, null=False, verbose_name='Digito verificador')
    
    class Meta:
        verbose_name='Personal'
        verbose_name_plural='Empleados'
        ordering=['per_email']

    def __str__(self):
        return self.per_email
    
class administrador(models.Model):
    adm_email = models.EmailField(max_length=32, primary_key=True)
    adm_password = models.CharField(max_length=32, blank=False, null=False)

    class Meta:
        verbose_name='Administrador'
        verbose_name_plural='Administradores'
        ordering=['adm_email']

    def __str__(self):
        return self.adm_email

class pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True, null=False, blank=False, editable=False, verbose_name='Nro identificador pedido')
    cli_email = models.ForeignKey(cliente, on_delete=models.PROTECT, verbose_name='Email cliente')
    fecha_pedido = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha pedido')
    total_pedido = models.IntegerField(verbose_name='Valor total del pedido', default=0)
    direccion_entrega = models.CharField(max_length=30, verbose_name='Dirección entrega pedido')#revisar la relacion de este campo con agregar una nueva direccion a la cuenta
    estado = models.CharField(max_length=15, verbose_name='Estado pedido', default='Procesando')

    class Meta:
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'
        ordering=['id_pedido']

    def __int__(self):
        return self.id_pedido

class item_compra(models.Model):
    item_id = models.AutoField(primary_key=True, editable=False, blank=False, verbose_name='Nro identificador item compra')
    item_cantidad = models.IntegerField(verbose_name='Cantidad de item de compra')
    item_precio_unitario = models.IntegerField(verbose_name='Precio unitario del item')
    total_item = models.IntegerField(verbose_name='Total item')#total_item = item_precio_unitario * item_cantidad
    id_pedido = models.ForeignKey(pedido, on_delete=models.PROTECT, verbose_name='Nro identificador pedido')
    prod_id = models.ForeignKey('producto', on_delete=models.PROTECT, verbose_name='Nro identificador producto')

    class Meta:
        verbose_name='Item compra'
        verbose_name_plural='Items compra'
        ordering=['item_id']

    def __int__(self):
        return self.item_id

class producto1(models.Model): #actualizar el nombre una vez quitados los modelos antiguos
    prod_id = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='Nro identificador producto')
    prod_marca = models.CharField(max_length=30, verbose_name='Marca producto')
    prod_modelo = models.CharField(max_length=30, verbose_name='Modelo producto')
    prod_precio = models.IntegerField(null=False, verbose_name='Precio producto')
    prod_descripcion = models.CharField(max_length=50, default='Descripción producto', verbose_name='Descripción producto')
    prod_stock = models.IntegerField(default=0, verbose_name='Stock producto')
    prod_imagen = models.CharField(max_length=100, default= 'Sin_imagen', verbose_name='Nombre imagen producto')#se almacenan de manera local, pero pueden ser urls
    cat_id = models.ForeignKey('categoria', on_delete=models.PROTECT, verbose_name='Nro id categoria')

    class Meta:
        verbose_name='Producto1'
        verbose_name_plural='Productos1'
        ordering=['prod_id']

    def __int__(self):
        return self.prod_id

class categoria1(models.Model): #actualizar el nombre una vez quitados los modelos antiguos
    cat_id = models.AutoField(primary_key=True,null=False, blank=False, verbose_name='Nro identificador categoria')
    cat_nombre= models.CharField(max_length=30, verbose_name='Nombre categoria')

    class Meta:
        verbose_name='Categoria1'
        verbose_name_plural='Categorias1'
        ordering=['cat_id']

    def __int__(self):
        return self.cat_id
    
#Cupones
class cupon(models.Model):
    cup_id = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='Identificador cupon')
    cup_nombre = models.CharField(max_length=10, verbose_name='Nombre cupon')
    cup_desc = models.CharField(max_length=30, verbose_name='Descripción cupon')
    cup_categoria = models.CharField(max_length=30, verbose_name='Categoria cupon')
    cup_fecha_inicio = models.DateField(verbose_name='Fecha inicio cupon')
    cup_fecha_termino = models.DateField(verbose_name='Fecha termino cupon')
    cup_porc_desc = models.IntegerField(default=0, verbose_name='Porcentaje de descuento', help_text='Solo ingresar números', validators=[MinValueValidator(1), MaxValueValidator(100)])
    cup_stock = models.IntegerField(default=0, verbose_name='Nro de cupones disponibles')

    class Meta:
        verbose_name='Cupon'
        verbose_name_plural='Cupones'
        ordering=['cup_id']

    def __int__(self):
        return self.cup_id
    
class cupon_usado(models.Model):
    cu_id = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='Nro ID cupon usado')
    cu_nombre_cupon = models.ForeignKey(cupon, on_delete=models.PROTECT, verbose_name='Nombre cupon canjeado')
    cu_cantidad_desc_compra = models.IntegerField(verbose_name='Valor del descuento aplicado',default=0)
    cu_fecha_canje = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha canje')
    cli_email = models.ForeignKey(cliente, verbose_name='Cliente canje', on_delete=models.PROTECT)

    class Meta:
        verbose_name='Cupon usado'
        verbose_name_plural='Cupones usados'
        ordering=['cu_id']

    def __int__(self):
        return self.cu_id