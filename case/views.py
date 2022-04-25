from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import *

# Начальная функция вывода главной страницы.
from django.template import RequestContext


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


class login(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    #template_name = 'registration/signup.html'