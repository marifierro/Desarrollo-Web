from django import forms
from django.forms import ModelForm
from .models import Libro

class LibroForm(ModelForm):

    class Meta:
        modelo= Libro
        fields = ['isbn', 'nombrelibro', 'autor', 'descripcion', 'categoria']