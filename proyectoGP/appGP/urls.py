from . import views
from django.contrib import admin
from django.urls import path, include 


urlpatterns = [

    path('listadoDeProyectos/', views.listaProyectos, name='listaP'),
    path('proyectos/<int:id_proyecto>/', views.detalleProyecto, name='detalleProyecto'),
    
]