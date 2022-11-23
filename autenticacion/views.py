from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate




# Create your views here.
def inicio(request):  # vista inicio para url
    return render(request, "app/index.html")

def register(request): # vista login para url

    data = {'form': SignUpForm}
    if request.method == 'POST':
        formulario = SignUpForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()


            usuario = authenticate(username = formulario.cleaned_data['username'],
                                   password = formulario.cleaned_data['password1'])

            login(request, usuario)
            return redirect('Inicio')

        else:
            messages.error(request,'No se pudieron validar los datos. intentalo de nuevo')

        data['form'] = formulario

    return render(request, 'registro.html', data)