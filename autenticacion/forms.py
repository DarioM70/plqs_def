from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Class registro
class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': "input-login",
            'placeholder': "Usuario*",
            'name': "usuario",
            'type': "text",
            'required': "True"
        })

        self.fields['email'].widget.attrs.update({
            'class': "input-login",
            'placeholder': "Correo*",
            'name': "correo",
            'type': "email",
            'required': "True"
        })

        self.fields['password1'].widget.attrs.update({
            'class': "input-login",
            'placeholder': "Contraseña*",
            'name': "contraseña",
            'type': "password",
            'required': "True"
        })

        self.fields['password2'].widget.attrs.update({
            'class': "input-login",
            'placeholder': "Confirmar contraseña*",
            'name': "contraseña",
            'type': "password",
            'required': "True"
        })

        self.fields['first_name'].widget.attrs.update({
            'class': "input-login",
            'placeholder': "Nombre(s)*",
            'name': "first_name",
            'type': "text",
            'required': "True"
        })

        self.fields['last_name'].widget.attrs.update({
            'class': "input-login",
            'placeholder': "Apellido*",
            'name': "last_name",
            'type': "text",
            'required': "True"
        })




    """ Formulário para inicializació de usuário """
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
