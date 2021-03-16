from django.contrib import admin

# Register your models here.

from .models import contacto
from .models import descripcion
from .models import carrusel
from .models import servicios
from .models import empresas

admin.site.register(contacto)
admin.site.register(descripcion)
admin.site.register(carrusel)
admin.site.register(servicios)
admin.site.register(empresas)