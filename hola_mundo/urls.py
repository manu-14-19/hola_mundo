from django.contrib import admin
from django.urls import path
from inicio.views import hola_mundo, saludo, sobre_mi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hola_mundo),
    path('saludo/<str:nombre>/', saludo),
    path('sobre-mi/', sobre_mi),
]