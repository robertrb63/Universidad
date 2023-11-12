from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo = models.CharField(max_length=5)
    poblacion = models.CharField(primary_key=True,max_length=50)
    telparroquia= models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telparroco= models.CharField(max_length=9)
    emailparroco= models.CharField(max_length=50)
    unidadpastoral = models.CharField(max_length=50)
    encargadounidad = models.CharField(max_length=50)
    telunidadpastoral = models.CharField(max_length=9)
    arciprestazgo = models.CharField(max_length=50)
    arcipreste = models.CharField(max_length=50)
    telarcipreste = models.CharField(max_length=9)
    
    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.poblacion, self.telparroquia, self.nombre, self.apellidos, self.telparroco, self.emailparroco, self.unidadpastoral, self.encargadounidad, self.telunidadpastoral, self.arciprestazgo, self.arcipreste, self.telarcipreste)