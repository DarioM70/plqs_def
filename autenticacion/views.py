from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import SignUpForm
from django.contrib.auth import login, authenticate




# Create your views here.

def redirect(request): # vista redirect para urls
    return render(request, 'login_redirect.html')

class LoginView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'registro.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            usuario = form.save()

            login(request, usuario)

            return redirect('redirect')

        else:
            return HttpResponse('hola')
    
    









