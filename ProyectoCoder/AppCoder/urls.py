from django.urls import path
from AppCoder import views


urlpatterns = [
   
    path('inicio', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name ="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name ="Estudiantes"),
    path('entregables', views.entregables, name ="Entregables"),
    path('cursosFormulario', views.cursosFormulario, name ="cursosFormulario"),
    path('estudiantesFormulario', views.estudiantesFormulario, name ="estudiantesFormulario"),
    path('profesoresFormulario', views.profesoresFormulario, name ="profesoresFormulario"),
]