from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='listaE'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('empresaAPP/', include('empresaAPP.urls')),
]
