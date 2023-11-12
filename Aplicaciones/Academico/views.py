from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages


# Create your views here.
def home(request):  
    cursoslist = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos":cursoslist})


def edicionCurso(request, poblacion):
    curso = Curso.objects.get(poblacion=poblacion)
    return render(request, "edicionCurso.html", {"curso": curso})


def editarCurso(request):
    codigo = request.POST['txtCodigo']
    poblacion = request.POST['txtNombre']
    telparroquia = request.POST['txtTelparroquia']
    nombre = request.POST['txtNombre']
    apellidos = request.POST['txtApellidos']
    telparroco = request.POST['txtParroco']
    emailparroco = request.POST['txtEmailparroquia']
    laico = request.POST['txtLaico']
    tellaico = request.POST['txtTellaico']
    unidadpastoral = request.POST['txtUnidadpastoral']
    encargadounidad = request.POST['txtEncargadounidad']
    telunidadpastoral = request.POST['txtUnidadpastoral']
    arciprestazgo = request.POST['txtArciprestazgo']
    arcipreste = request.POST['txtArcipreste']
    telarcipreste = request.POST['txtPTelarcipreste']

    curso = Curso.objects.get(poblacion=poblacion)
    curso.codigo=codigo
    curso.poblacion = poblacion
    telparroquia = telparroquia
    curso.nombre = nombre
    apellidos = apellidos
    telparroco = telparroco
    laico = laico
    tellaico = tellaico
    emailparroco = emailparroco
    unidadpastoral = unidadpastoral
    encargadounidad = encargadounidad
    telunidadpastoral = telunidadpastoral
    arciprestazgo = arciprestazgo
    arcipreste = arcipreste
    telarcipreste = telarcipreste
    curso.save()
    return redirect('/')

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    poblacion = request.POST['txtPoblacion']
    telparroquia = request.POST['txtParroquia']
    nombre = request.POST['txtNombre']
    apellidos = request.POST['txtApellidos']
    telparroco = request.POST['txtParroco']
    emailparroco = request.POST['txtEmailparroquia']
    laico = request.POST['txtLaico']
    tellaico = request.POST['txtTellaico']
    unidadpastoral = request.POST['txtUnidadpastoral']
    encargadounidad = request.POST['txtEncargadounidad']
    telunidadpastoral = request.POST['txtUnidadpastoral']
    arciprestazgo = request.POST['txtArciprestazgo']
    arcipreste = request.POST['txtArcipreste']
    telarcipreste = request.POST['txtPTelarcipreste']


    curso = Curso.objects.create(codigo=codigo, poblacion=poblacion, telparroquia=telparroquia, nombre=nombre, apellidos=apellidos , telparroco=telparroco, emailparroco=emailparroco, laico=laico, tellaico=tellaico, unidadpastoral=unidadpastoral, encargadounidad=encargadounidad, telunidadpastoral=telunidadpastoral, arciprestazgo=arciprestazgo, arcipreste=arcipreste, telarcipreste=telarcipreste)
    
    messages.success(request, '¡Cursos Registrado!')
    return redirect('/')    

def eliminarCurso(request, poblacion):
    curso = Curso.objects.get(poblacion=poblacion)
    curso.delete()
    return redirect('/')