from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request): # vista inicio para url
    return render(request, "app/index.html")


def servicios(request):# vista servicio para url
    return render(request, "app/servicios.html")


def contacto(request): # vista contacto para url
    return render(request, "app/contacto.html")


def registrarse(request): # vista registro para url
    return render(request, "app/registro.html")


def iniciar(request): # vista inicio de sesion para url
    return render(request, "app/iniciar.html")