from django.urls import path

from app import views

#conf djanfo para mostrar imagenes
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('servicios/', views.servicios, name="Servicios"),

    path('contacto/', views.contacto, name="Contacto"),
    path('iniciar/', views.iniciar, name="Iniciar sesion"),

]

#mostrar imagenes
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)