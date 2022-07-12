from multiprocessing import context
from django.contrib import messages
from http.client import HTTPResponse
from django.contrib.auth import logout
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Usuario, Categoria
from .models import Producto
from api.views import *
from .forms import ProductoForm
# Create your views here.

#---Funciones de REGISTRO---
def registro1(request):
    return render(request, 'registro1.html')

def registro2(request):
    return render(request, 'registro2.html')

#---Funciones de LOGIN---
def login(request):
    return render(request, 'login.html')

def perfil(request):
    return render(request,'perfil.html')

def admin_productos(request):
    form = ProductoForm()
    producto = Producto.objects.all()
    datos={'producto':producto,'form':form}

    return render(request,'admin_productos.html',datos)

def admin_edit(request):
    form = ProductoForm()
    producto = Producto.objects.all()
    datos={'producto':producto,'form':form}

    return render(request, 'admin_edit.html', datos)

def contactanos(request):
    return render(request,'contactanos.html')

#Recibimos los datos del formulario via POST
def validarusuario(request):
    v_correo = request.POST.get('loginEmail')
    v_pass = request.POST.get('loginPassword')
    try:
    #Buscamos el usuario en la base de datos
        usu=Usuario.objects.get(email=v_correo, password=v_pass)
        
        if usu:
            request.session['usuario'] = v_correo
            return redirect('/perfil')

    except:
        return redirect('/login')
#Esta funcion evita entrar a perfil directo
def perfil(request):
    if 'usuario' not in request.session:
        return redirect('/login')
    else:
        return render(request, 'perfil.html')

#---------------Fin funciones de login-----------------

#--------------Registro de data BBDD-------------------
def registrarUsuario(request):
    #obtiene datos desde el formulario en registro
    r_correo = request.POST.get('registroEmail')
    r_nombre = request.POST.get('registroNombre')
    r_pass1 = request.POST.get('passwordRegistro1')
    r_pass2 = request.POST.get('passwordRegistro2')
    if r_pass1 == r_pass2:
    #Registra al usuario en la BBDD
        nuevo_usuario=Usuario()
        nuevo_usuario.email=r_correo
        nuevo_usuario.nombre=r_nombre
        nuevo_usuario.password=r_pass1
        Usuario.save(nuevo_usuario)
        return redirect('/registrado')#crear un post registro como logout
    else:
        mensaje = 'Las contraseñas no coinciden.'
        return HttpResponse(mensaje)
#-----------------Fin registro data BBDD-----------------

#funcion busqueda test
def buscarUsuario(request, p_email):
    buscado=Usuario.objects.get(email=p_email)
    datos={'usuario': buscado}
    return render(request, 'modificar.html', datos)


#metodo de logout
def pagina_logout(request):
    return render(request,'logout.html')

#metodo registrado
def registrado(request):
    return render(request,'registrado.html')


#funcion cerrar sesion
def cerrar_sesion(request):
    if 'usuario' in request.session:
        logout(request)
        return redirect('/logout')
    else:
        return redirect('/logout')

#--------Funciones de editar/eliminar productos
def guardarProducto(request):
    #pasando la data a las variables
    v_categoria=request.POST.get('categoria')
    v_nombre_producto=request.POST.get('nombre_producto')
    v_precio_producto=request.POST.get('precio_producto')
    v_stock_producto=request.POST.get('stock_producto')
    v_descripcion_producto=request.POST.get('descripcion_producto')
    v_imagen=request.POST.get('imagen')
    
    nuevo=Producto()
    nuevo.categoria= Categoria.objects.get(id = request.POST['categoria'])
    nuevo.nombre_producto=v_nombre_producto
    nuevo.precio_producto=v_precio_producto
    nuevo.stock_producto=v_stock_producto
    nuevo.descripcion_producto=v_descripcion_producto
    nuevo.imagen= v_imagen

    #guarda la data del objeto
    Producto.save(nuevo)

    return redirect('/admin_productos')

#Buscar producto
def buscarProducto(request, p_id):
    buscado=Producto.objects.get(id=p_id)
    datos={'producto': buscado}
    return render(request, 'admin_edit.html', datos)

#modificar productos
def guardarProductoModificado(request):
    v_id=request.POST.get('id')
    v_categoria=request.POST.get('categoria')
    v_nombre_producto=request.POST.get('nombre_producto')
    v_precio_producto=request.POST.get('precio_producto')
    v_stock_producto=request.POST.get('stock_producto')
    v_descripcion_producto=request.POST.get('descripcion_producto')
    v_imagen=request.POST.get('imagen')
    
    buscado=Producto.objects.get(id=v_id)

    if(buscado):
        buscado.categoria_id=v_categoria
        buscado.nombre_producto=v_nombre_producto
        buscado.precio_producto=v_precio_producto
        buscado.descripcion_producto=v_descripcion_producto
        buscado.nombre_producto=v_nombre_producto
        buscado.imagen=v_imagen
        buscado.stock_producto=v_stock_producto

        Producto.save(buscado)
        return redirect('/admin_productos')

#eliminar productos
def eliminarProducto(request, p_id):
    buscado=Producto.objects.get(id=p_id)
    if(buscado):
        Producto.delete(buscado)
        return redirect('/admin_productos')
