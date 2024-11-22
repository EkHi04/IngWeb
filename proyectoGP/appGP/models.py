from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    fecha_entrega = models.DateField(null=True, blank=True)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estado = models.CharField(
        max_length=50,
        choices=[('active', 'Activo'), ('completed', 'Completado'), ('paused', 'En pausa')],
        default='active'
    )
    
    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    fecha_entrega = models.DateField(null=True, blank=True)
    proyecto = models.ForeignKey(Proyecto, related_name='tareas', on_delete=models.CASCADE)
    tiempo_estimado = models.DurationField(null=True, blank=True)  # Duración estimada en formato hh:mm:ss
    prioridad = models.CharField(
        max_length=20,
        choices=[('Urgent', 'Urgente'), ('Normal', 'Normal'), ('Optional', 'Opcional')],
        default='Normal'
    )
    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre= models.CharField(max_length=100)
    dni= models.TextField(max_length=8)
    telefono = models.CharField(max_length=9, blank=True)
    edad = models.PositiveIntegerField()
    tarea = models.ForeignKey(Tarea, related_name="personas", on_delete=models.CASCADE)
    correo_electronico = models.EmailField(max_length=254, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    rol = models.CharField(
        max_length=50,
        choices=[('Manager', 'Manager'), ('Developer', 'Desarrollador'), ('Tester', 'Tester')],
        default='Developer'
    )
    ImagenPersona = models.URLField(max_length=600, null=True, blank=True)
    
    def __str__(self):
        return self.nombre
