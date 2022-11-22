from django.urls import path

from autenticacion import views


"""#conf djanfo para mostrar imagenes
from django.conf import settings
from django.conf.urls.static import static"""

urlpatterns = [
    path('registro/', views.LoginView.as_view(), name="Registrarse"),
    path('redirect/', views.redirect, name="Login"),


]