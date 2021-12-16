from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante, Profesor

# Create your views here.

def inicio (request):

    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    
    return render(request, 'AppCoder/entregables.html')

def cursosFormulario(request):

    if request.method == "POST":
        curso = Curso(nombre=request.POST["nombre"], comision=request.POST["comision"])
        curso.save()

        return render(request, 'AppCoder/inicio.html')

    return render (request, 'AppCoder/cursosFormulario.html')


def estudiantesFormulario(request):

    if request.method == "POST":
        estudiante = Estudiante(nombre=request.POST["nombre"], apellido=request.POST["apellido"], email=request.POST["email"])
        estudiante.save()

        return render(request, 'AppCoder/inicio.html')

    return render (request, 'AppCoder/estudiantesFormulario.html')


def profesoresFormulario(request):

    if request.method == "POST":
        profesor = Profesor(nombre=request.POST["nombre"], apellido=request.POST["apellido"], email=request.POST["email"], profesion=request.POST["profesion"])
        profesor.save()

        return render(request, 'AppCoder/inicio.html')



    return render (request, 'AppCoder/profesoresFormulario.html')


