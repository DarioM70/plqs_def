from django.urls import path

from app import views

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('servicios/', views.servicios, name="Servicios"),
    path('contacto/', views.contacto, name="Contacto"),
    path('registro/', views.registrarse, name="Registrarse"),
    path('iniciar/', views.iniciar, name="Iniciar sesion"),

]