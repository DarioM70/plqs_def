from django.shortcuts import render, HttpResponse

from  servicios.models import Servicios

# Create your views here.

def inicio(request): # vista inicio para url
    return render(request, "app/index.html")


def servicios(request): # vista servicio para url

    servicios = Servicios.objects.all()
    return render(request, "app/servicios.html", {"servicios": servicios})


def contacto(request): # vista contacto para url
    return render(request, "app/contacto.html")


def registrarse(request): # vista registro para url
    return render(request, "app/registro.html")


def iniciar(request): # vista inicio de sesion para url
    return render(request, "app/iniciar.html")

