from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from .forms import *

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def consulta(request):
    return render(request, 'consulta.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirecionar para a página de login após o registro
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('consulta')  # Redirecionar para a página inicial após o login
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)  # Chama a função logout para desconectar o usuário
    return redirect('login')  # Redireciona para a página de login após o logout
