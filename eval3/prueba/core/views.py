from django.shortcuts import render
from .models import Libro
from .forms import LibroForm

# Create your views here.

def home(request):
    libros= Libro.objects.all()
    datos = {
        'libros': libros
    }
    return render(request, 'core/index.html', datos)

def form_libro(request):
    datos= {
        'form': LibroForm()
    }
    if request.method== 'POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"
            
    return render(request, 'core/form_libro.html', datos)