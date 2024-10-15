from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def busqueda_productos(request):

    return render(request, "busqueda.html")

def buscar(request):
    mensaje="Articulo Buscado: %r" %request.GET["prd"]
    return HttpResponse(mensaje)

