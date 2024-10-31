from django.contrib import admin
from .models import Proyecto, Tarea, Usuario

admin.site.register(Proyecto)
admin.site.register(Tarea)
admin.site.register(Usuario)
