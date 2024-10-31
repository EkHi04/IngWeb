from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    proyecto = models.ForeignKey(Proyecto, related_name='tareas', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, related_name='tareas_usuario', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username
