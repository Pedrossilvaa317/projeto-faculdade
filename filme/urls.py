from django.urls import path
from .views import list_filmes

app_name = 'filme'

urlpatterns = [
    path('list_filmes/',list_filmes, name='list_filmes'),

]