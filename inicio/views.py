from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hola_mundo(request):
    return render(request, 'inicio/hola_mundo.html')

def saludo(request, nombre):
    contexto = {
        'nombre': nombre,
        'mensaje': '¡Bienvenido a mi página!',
    }
    return render(request, 'inicio/saludo.html', contexto)