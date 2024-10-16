from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.conf import settings
from django.core.mail import send_mail

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

        subject=request.POST["asunto"]
        message=request.POST["mensaje"] +" "+ request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["lulito131@gmail.com"]

        send_mail(subject,message,email_from,recipient_list)
        
        return render (request, "gracias.html")
  
    return render (request, "contactenos.html")