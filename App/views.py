from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'App/home.html')


def registro(request):
    data = {

        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        print(request.POST)

        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'],
                                password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Te has registrado sastifactoriamente')
            return redirect(to='home')
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)
