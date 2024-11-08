from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Proyecto, Tarea, Persona

def listaProyectos(request):
    proyectos = Proyecto.objects.order_by('nombre')
    nombres_proyectos = ', '.join([proyecto.nombre for proyecto in proyectos])
    return HttpResponse(nombres_proyectos)

def listadeTareas(request):
    tareas = Tarea.objects.order_by('nombre')
    nombres_tareas = ', '.join([tarea.nombre for tarea in tareas])
    return HttpResponse(nombres_tareas)

def listadePersonas(request):
    personas = Persona.objects.order_by('nombre')
    context = {'personas' : personas}
    return render(request,'listaPersonas.html', context)

def detalleProyecto(request, id_proyecto):
    try:
        proyecto = Proyecto.objects.get(pk=id_proyecto)
        tareas = proyecto.tareas.all()

        cadenaDeTexto = f"{proyecto.nombre} - Descripción: {proyecto.descripcion} - Fecha Creacion: {proyecto.fecha_creacion} - Fecha Entrega: {proyecto.fecha_entrega}\n"

        if tareas.exists():
            cadenaDeTexto += "Tareas:\n"
            for tarea in tareas:
                cadenaDeTexto += f"- {tarea.nombre}, Fecha de entrega: {tarea.fecha_entrega}\n"
        else:
            cadenaDeTexto += "No hay tareas asociadas a este proyecto."

        return HttpResponse(cadenaDeTexto)
    except Proyecto.DoesNotExist:
        return HttpResponseNotFound("Proyecto no encontrado")
    
def detalleTarea(request, id_tarea):
    try:
        tarea = Tarea.objects.get(pk=id_tarea)
        personas = tarea.personas.all()



        cadenaDeTexto = f"{tarea.nombre} - Descripción: {tarea.descripcion} - Fecha Creacion: {tarea.fecha_creacion} - Fecha Entrega: {tarea.fecha_entrega}\n"

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

        cadenaDeTexto = f"{persona.nombre} - Dni: {persona.dni}  - Telefono: {persona.telefono}  - Edad: {persona.edad} -  \n"

        

        return HttpResponse(cadenaDeTexto)
    except Persona.DoesNotExist:
        return HttpResponseNotFound("Tarea no encontrada")
    
    
