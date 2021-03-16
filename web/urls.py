from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('productos', views.productos),
    path('sistemas', views.sistemas),
    path('cercos', views.cercos),
    path('control', views.control),
    path('seguridad', views.seguridad),
    path('selectricos', views.selectricos),
]