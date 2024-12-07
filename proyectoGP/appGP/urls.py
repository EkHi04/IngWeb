from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [

    path('', views.index, name='index'),

    path('listadoDeProyectos/', views.listadeProyectos, name='listaP'),
    path('listadoDeTareas/', views.listadeTareas, name='listaT'),
    path('listadoDePersonas/', views.listadePersonas, name='listaPer'),

    path('proyectos/<int:id_proyecto>/', views.detalleProyecto, name='detalleProyecto'),
    path('personas/<int:id_persona>/', views.detallePersona, name='detallePersona'),
    path('tareas/<int:id_tarea>/', views.detalleTarea, name='detalleTarea'), 
  
]

