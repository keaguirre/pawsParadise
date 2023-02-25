from django.contrib import admin
from .models import Usuario, Producto, Categoria
from .models import cliente, personal_tienda, administrador, pedido, item_compra, producto1, categoria1, cupon, cupon_usado

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Categoria)
#------------------------------
admin.site.register(cliente)
admin.site.register(personal_tienda)
admin.site.register(administrador)
admin.site.register(pedido)
admin.site.register(item_compra)
admin.site.register(producto1)
admin.site.register(categoria1)
admin.site.register(cupon)
admin.site.register(cupon_usado)