from django.urls import path
from . import views

urlpatterns = [
    path('listadoDeProyectos/', views.listaProyectos, name='listaP'),
    path('proyectos/<int:id_proyecto>/', views.detalleProyecto, name='detalleProyecto'),
]
