from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
# Create your views here.

def busqueda_productos(request):

    return render(request, "busqueda.html")

def buscar(request):

    if request.GET["prd"]:
        
        mensaje="Articulo Buscado: %r" %request.GET["prd"]
        producto=request.GET["prd"]
        if len(producto)>30:
            mensaje="Texto de Busqueda demasiado largo"

        else: 
            articulos=Articulos.objects.filter(nombre__icontains=producto) #icontrains funciona como el Like del SQL
            return render(request, "resultados_busqueda.html",{"articulos":articulos, "query":producto})

    else:
        
        mensaje="No se puede dejar en blanco"

    return HttpResponse(mensaje)

def contacto(request):

    if request.method=="POST":

        return render (request, "gracias.html")
  
    return render (request, "contactenos.html")