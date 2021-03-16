from django.db import models

# Create your models here.

class contacto(models.Model):
    correo = models.CharField(max_length=200)
    numero = models.IntegerField()

class descripcion(models.Model):
    texto = models.CharField(max_length=1000)

class carrusel(models.Model):
    texto = models.CharField(max_length=500)
    imagen = models.ImageField(null=True, upload_to="carrusel")

class servicios(models.Model):
    titulo = models.CharField(max_length=500)
    texto = models.CharField(max_length=500)
    imagen = models.ImageField(null=True, upload_to="servicios")

class empresas(models.Model):
    texto = models.CharField(max_length=500)
    imagen = models.ImageField(null=True, upload_to="empresas")