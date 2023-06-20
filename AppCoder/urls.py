from django.urls import path
from .views import inicio, cursos, entregables, estudiantes, profesores


urlpatterns = [

    path('inicio/', inicio, name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('entregables/', entregables, name="Entregables"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('profesores/', profesores, name="Profesores"),
]