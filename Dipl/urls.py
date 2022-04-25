from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('case/', include('case.urls')),
    # Всегда переходит на ссылку сайта проекта
    path('', RedirectView.as_view(url='/case/', permanent=True)),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
