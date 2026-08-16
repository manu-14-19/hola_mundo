from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hola_mundo(request):
    return render(request, 'inicio/hola_mundo.html')

def saludo(request, nombre):
    contexto = {
        'nombre': nombre,
        'mensaje': '¡Esta página fue creada por Manuela!',
    }
    return render(request, 'inicio/saludo.html', contexto)

def sobre_mi(request):
    return render(request, 'inicio/sobre_mi.html')