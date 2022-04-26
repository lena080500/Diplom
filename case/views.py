from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from .forms import CaseForm
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
        #{'cases': cases} передать всю информацию о кейсах
    )


# Начальная функция вывода страницы кейсов.
def case(request):
    error = ''
    if request.method == 'POST': #Происходит ли считывание с сайта
        form = CaseForm(request.POST) #добавили данные в form с сайта
        if form.is_valid(): #Являются ли данные корректно заполненными
            form.save() #сохрание в базу данных
            #return redirect('') - переадресация на др станицу, если все добавилось
        else: error = 'Форма была неверной'

    form = CaseForm()

    data = {
        'form': form,
        'error': error
    }

    return render(
        request,
        'cases.html',
        data
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


def param(request):
    parametr = CaseParametr.objects.get(pk=1)
    CaseParametr.newFormula(parametr)
    return render(
        request,
        'param.html',
        #{'parametr': parametr}
    )


class Login(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    #template_name = 'registration/signup.html'
