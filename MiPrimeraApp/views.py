from django.shortcuts import render
from django.http import HttpResponse
# se importa para trer los registros en el modelo
from .models import Libros
from .form import LibrosForm

# Create your views here.
def inicio(request):
    numero1= 3
    numero2= 6
    resultado= numero1 + numero2
    
    return HttpResponse(f"<h1> Bienvenido a mi primera Web </h1><br><br>\n El resulado de {numero1} mas {numero2} es {resultado}")
def presentacion(request):
    return render(request, 'paginas/presentacion.html')

def libros(request):
    # se crea la variable a donde se asignaran todos los libros
    libros=Libros.objects.all()
    return render(request, 'paginas/index.html', {'libros': libros})

def crear(request):
    formulario=LibrosForm(request.POST or None)
    return render(request, 'paginas/crear.html', {'formulario':formulario})

def editar(request):
    return render(request, 'paginas/editar.html')
