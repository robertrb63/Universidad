from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<poblacion>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<poblacion>', views.eliminarCurso)
]