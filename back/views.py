from http.client import HTTPResponse
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Usuario
# Create your views here.

#---Funciones de REGISTRO---
def registro1(request):
    return render(request, 'registro1.html')

def registro2(request):
    return render(request, 'registro2.html')

#Recibimos los datos del formulario via POST
#def registrarusuario(request):
    v_nombre = request.POST.get('nombre')
    v_correo = request.POST.get('email')
    v_pass1 = request.POST.get('pass1')
    v_pass2 = request.POST.get('pass2')
    #if v_pass1 == v_pass2:
        #Si ambas son iguales entonces que registre v_pass1




#---Funciones de LOGIN---
def login(request):
    return render(request, 'login.html')

def perfil(request):
    return render(request,'perfil.html')
def contactanos(request):
    return render(request,'contactanos.html')

#Recibimos los datos del formulario via POST
def validarusuario(request):
    v_correo = request.POST.get('email')
    v_pass = request.POST.get('password')
    #return HttpResponse("LALALALA")
    try:
    #Buscamos el usuario en la base de datos
        usu=Usuario.objects.get(email=v_correo, password=v_pass)

        
        if usu:
            request.session['usuario'] = v_correo
            return redirect('/perfil')

    except:
        return redirect('/carro')
#Esta funcion evita entrar a perfil directo
def perfil(request):
    if 'usuario' not in request.session:
        return redirect('/login')

    return render(request, 'perfil.html')
