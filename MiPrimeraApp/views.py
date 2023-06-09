from django.shortcuts import render, redirect
from django.http import HttpResponse
# se importa para trer los registros en el modelo
from .models import Libro
from .form import LibroForm

# Create your views here.
def inicio(request):
    numero1= 3
    numero2= 6
    resultado= numero1 + numero2
    
    return HttpResponse(f"<h1> Bienvenido a mi primera Web </h1><br><br>\n El resulado de {numero1} mas {numero2} es {resultado}")
def presentacion(request):
    return render(request, 'paginas/presentacion.html')

def libro(request):
    # se crea la variable a donde se asignaran todos los libros
    libros=Libro.objects.all()
    return render(request, 'paginas/index.html', {'libros': libros})

def crear(request):
    formulario=LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    
    return render(request, 'paginas/crear.html', {'formulario':formulario})

def editar(request, id):
    
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid and request.method=='POST':
        formulario.save()
        return redirect('libros')
    return render (request, 'paginas/editar.html', {'formulario': formulario})
   
    
def eliminar(request,id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')