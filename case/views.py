from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import *
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Начальная функция вывода главной страницы.
def main(request):
    cases = Case.objects.all()
    return render(
        request,
        'main.html',
    )


# Начальная функция вывода страницы кейсов.
def case(request):
    return render(
        request,
        'cases.html',
    )


def login(request):
    return render(
        request,
        'registration.html',
    )


def contacts(request):
    return render(
        request,
        'contacts.html',
    )


def search(request):
    return render(
        request,
        'contacts.html',
    )


class Login(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    #template_name = 'registration/signup.html'