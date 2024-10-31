from django.http import HttpResponse, HttpResponseNotFound
from .models import Proyecto

def listaProyectos(request):
    proyectos = Proyecto.objects.order_by('nombre')
    nombres_proyectos = ', '.join([proyecto.nombre for proyecto in proyectos])
    return HttpResponse(nombres_proyectos)

def detalleProyecto(request, id_proyecto):
    try:
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        tareas = proyecto.tareas.all()

        cadenaDeTexto = f"{proyecto.nombre} - Descripción: {proyecto.descripcion}\n"

        if tareas.exists():
            cadenaDeTexto += "Tareas:\n"
            for tarea in tareas:
                cadenaDeTexto += f"- {tarea.nombre}, Fecha de entrega: {tarea.fecha_entrega}\n"
        else:
            cadenaDeTexto += "No hay tareas asociadas a este proyecto."

        return HttpResponse(cadenaDeTexto)
    except Proyecto.DoesNotExist:
        return HttpResponseNotFound("Proyecto no encontrado")
