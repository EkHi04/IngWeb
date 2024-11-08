from django.db import models

class Proyecto(models.Model):
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    fecha_entrega = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    fecha_entrega = models.DateField(null=True, blank=True)
    proyecto = models.ForeignKey(Proyecto, related_name='tareas', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre= models.CharField(max_length=100)
    dni= models.TextField(max_length=8)
    telefono = models.CharField(max_length=9, blank=True)
    edad = models.PositiveIntegerField()
    tarea = models.ForeignKey(Tarea, related_name="personas", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
