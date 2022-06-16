from django.contrib import admin
from .models import Usuario, Pedido, Producto
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Pedido)
admin.site.register(Producto)