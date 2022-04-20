from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Начальная функция вывода страницы кейсов.
def cases(request):
    return render(
        request,
        "cases.html"
    )

# Начальная функция вывода главной страницы.
def main(request):
    return render(
        request,
        "main.html"
    )