from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Usuario

class RegistroForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['email','nombre_usuario', 'password']
