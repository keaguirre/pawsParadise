from django.shortcuts import render
from back.models import Producto


# Create your views here.

def homedehome(request):#home desde home
    return render(request,'index.html')

def backhome(request):#volver a home desde secciones
    return render(request,'index.html')

# views modelos



# views funciones | url
def comocomprar(request):
    return render(request,'secciones/comocomprar.html')

def alimento(request):
    producto = Producto.objects.filter(categoria_id=1)
    datos = {'producto':producto}
    return render(request,'secciones/Alimento.html', datos)

def bandanas(request):
    producto = Producto.objects.filter(categoria_id=4)
    datos = {'producto':producto}
    return render(request,'secciones/Bandanas.html',datos)
    
def carro(request):
    return render(request,'secciones/Carro.html')

def consultapi(request):
    return render(request,'secciones/consultApi.html')
    
def correas(request):
    producto = Producto.objects.filter(categoria_id=2)
    datos = {'producto':producto}
    return render(request,'secciones/Correas.html',datos)

def higiene(request):
    producto = Producto.objects.filter(categoria_id=3)
    datos = {'producto':producto}
    return render(request,'secciones/Higiene.html',datos)

def membresia(request):
    return render(request,'secciones/membresia.html')

def placas(request):
    producto = Producto.objects.filter(categoria_id=7)
    datos = {'producto':producto}
    return render(request,'secciones/placas.html',datos)

def registro1(request):
    return render(request,'secciones/registro1.html')

def registro2(request):
    return render(request,'secciones/registro2.html')

def ropa(request):
    producto = Producto.objects.filter(categoria_id=5)
    datos = {'producto':producto}
    return render(request,'secciones/ropa.html',datos)

























