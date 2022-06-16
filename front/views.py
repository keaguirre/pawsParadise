from django.shortcuts import render


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
    return render(request,'secciones/Alimento.html')

def bandanas(request):
    return render(request,'secciones/Bandanas.html')
    
def carro(request):
    return render(request,'secciones/Carro.html')

def consultapi(request):
    return render(request,'secciones/consultApi.html')
    
def correas(request):
    return render(request,'secciones/Correas.html')

def higiene(request):
    return render(request,'secciones/Higiene.html')

def membresia(request):
    return render(request,'secciones/membresia.html')

def placas(request):
    return render(request,'secciones/placas.html')

def registro1(request):
    return render(request,'secciones/registro1.html')

def registro2(request):
    return render(request,'secciones/registro2.html')

def ropa(request):
    return render(request,'secciones/ropa.html')

























