from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Proyecto, Tarea, Persona

def index(request):
    return render(request, 'index.html')


def listadeProyectos(request):
    proyectos = Proyecto.objects.all()  
    return render(request, 'listaProyectos.html', {'proyectos': proyectos})


def listadeTareas(request):
    tareas = Tarea.objects.order_by('fecha_creacion')
    context = {'tareas' : tareas}
    return render(request,'listaTareas.html', context)

def listadePersonas(request):
    personas = Persona.objects.order_by('dni')
    context = {'personas' : personas}
    return render(request,'listaPersonas.html', context)

def detalleProyecto(request, id_proyecto):
    try:
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        tareas = proyecto.tareas.all()

        cadenaDeTexto = f"{proyecto.nombre} - Descripción: {proyecto.descripcion} - Fecha Creacion: {proyecto.fecha_creacion} - Fecha Entrega: {proyecto.fecha_entrega} - Presupuesto: {proyecto.presupuesto}  - Estado del Proyecto: {proyecto.estado}\n"

        if tareas.exists():
            cadenaDeTexto += "Tareas:\n"
            for tarea in tareas:
                cadenaDeTexto += f"- {tarea.nombre}, Fecha de entrega: {tarea.fecha_entrega}\n"
        else:
            cadenaDeTexto += "No hay tareas asociadas a este proyecto."

        context = {'p' : proyecto, 'tareas':tareas}
        return render(request,'vistaproyectos.html',context)
    except Proyecto.DoesNotExist:
        return HttpResponseNotFound("Proyecto no encontrado")
    
def detalleTarea(request, id_tarea):
    try:
        tarea = Tarea.objects.get(pk=id_tarea)
        personas = tarea.personas.all()
        
        cadenaDeTexto = f"{tarea.nombre} - Descripción: {tarea.descripcion} - Fecha Creacion: {tarea.fecha_creacion} - Fecha Entrega: {tarea.fecha_entrega} - Tiempo Estimado: {tarea.tiempo_estimado} - Prioridad de la tarea: {tarea.prioridad}\n"

        if personas.exists():
            cadenaDeTexto += "Personas que contribuyen a esta tarea:\n"
            for persona in personas:
                cadenaDeTexto += f"- {persona.nombre}, Dni: {persona.dni}\n"
        else:
            cadenaDeTexto += "No hay personas asociadas a este proyecto."
        
        
        context = {'t' : tarea}
        return render(request,'vistatareas.html',context)
    except Tarea.DoesNotExist:
        return HttpResponseNotFound("Tarea no encontrada")
    
def detallePersona(request, id_persona):
    try:
        persona = Persona.objects.get(pk=id_persona)
        context = {'p' : persona}
        return render(request,'vistapersonas.html',context)
    except Persona.DoesNotExist:
        return HttpResponseNotFound("Tarea no encontrada")
    
    
