from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Producto, Usuario

class RegistroForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['email','nombre', 'password']

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['categoria', 'nombre_producto', 'precio_producto', 'stock_producto', 'descripcion_producto', 'imagen']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.TextInput(attrs={'class': 'form-control'}),
        }