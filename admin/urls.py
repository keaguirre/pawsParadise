"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from operator import index
from django.contrib import admin
from django.urls import path
from front.views import comocomprar
from front.views import alimento
from front.views import bandanas
from front.views import carro
from front.views import consultapi
from front.views import correas
from front.views import higiene
from front.views import membresia
from front.views import placas
from front.views import registro1
from front.views import registro2
from front.views import ropa
#---importando home
from front.views import backhome

#FROM back
from back.views import login, validarusuario, perfil
from back.views import contactanos
from back.views import registro1
from back.views import registro2



urlpatterns = [
    #Panel administrador
    path('admin/', admin.site.urls),
    
    #---path('Alias',NombreFuncion en views)
    path('',backhome, name='backhome'),#path para volver a home desde seccion
    
    #importando todas las secciones
    path('comocomprar',comocomprar),
    path('alimento',alimento),
    path('bandanas',bandanas),
    path('carro',carro),
    path('consultapi',consultapi),
    path('contactanos',contactanos),
    path('correas',correas),
    path('higiene',higiene),
    path('login',login),
    path('membresia',membresia),
    path('placas',placas),
    path('registro1',registro1),
    path('registro2',registro2),
    path('ropa',ropa),
    path('perfil',perfil),
    #Te lleva a perfil si es exitosa si no a login
    path('validarusuario',validarusuario),
]
