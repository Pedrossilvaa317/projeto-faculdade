from django.contrib import admin
from django.urls import path, include
from core.views import index


urlpatterns = [
    path('', index, name = 'index'),
    path('filmes/',include('filme.urls',namespace ='filme')),
    path('admin/', admin.site.urls),
]
