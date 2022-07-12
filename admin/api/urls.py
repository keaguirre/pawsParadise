from django.urls import path
from .views import traerProductos

urlpatterns= [
    path('traerProductos', traerProductos, name='traer_productos'),
]