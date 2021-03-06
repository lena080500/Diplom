from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),  # Начальная ссылка на функцию работы с данными моделей.
    path('case/', views.case, name='case'),
    path('login/', views.Login.as_view(), name='login'),
    path('contacts/', views.contacts, name='contacts'),
    path('param/', views.param, name='param'),
]

