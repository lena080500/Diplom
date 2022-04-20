from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),  # Начальная ссылка на функцию работы с данными моделей.
    path('case', views.case, name='case'),
]