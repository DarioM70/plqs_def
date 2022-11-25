from django.shortcuts import render

from servicios.models import Servicios
from .models import Colaboradores


# Create your views here.

def inicio(request):  # vista inicio para url
    colaboradores = Colaboradores.objects.all()
    return render(request, "app/index.html", {"colaboradores": colaboradores})


def servicios(request):  # vista servicio para url

    servicios = Servicios.objects.all()  # Obtengo datos del modelo
    return render(request, "app/servicios.html", {"servicios": servicios})


def contacto(request):  # vista contacto para url
    return render(request, "app/contacto.html")


def iniciar(request):  # vista inicio de sesion para url
    return render(request, "app/iniciar.html")
