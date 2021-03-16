from django.shortcuts import render
from .models import contacto
from .models import descripcion
from .models import carrusel
from .models import servicios
from .models import empresas

# Create your views here.

def index(request):
    contacto1 = contacto.objects.all()
    descripcion1 = descripcion.objects.all()
    carrusel1 = carrusel.objects.all()  
    servicios1 = servicios.objects.all()
    empresas1 = empresas.objects.all()
    context = {'contacto':contacto1,'descripcion':descripcion1,'servicios':servicios1,'empresas':empresas1,'carrusel':carrusel1}
    return render(request, 'index.html',context)

def productos(request):
    return render(request, 'productos.html')

def sistemas(request):
    return render(request, 'sistemas.html')

def cercos(request):
    return render(request, 'cercos.html')

def control(request):
    return render(request, 'control.html')

def seguridad(request):
    return render(request, 'seguridad.html')

def selectricos(request):
    return render(request, 'selectricos.html')