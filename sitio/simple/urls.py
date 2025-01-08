from django.urls import path
from . import views  # Importa las vistas de la aplicación

urlpatterns = [
    path('', views.index, name='index'),  # Ruta principal de la aplicación
    path('index', views.index, name='index'),
]