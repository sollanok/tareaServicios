from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),

    # Path para Crud de usuarios
    path('usuarios', views.usuarios, name = 'usuarios'),

    # Path para Crud de partidas
    path('partidas', views.partidas, name = 'partidas'),

]