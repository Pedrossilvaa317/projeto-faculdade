from django.urls import path
from .views import list_filmes,new_filmes


app_name = 'filme'

urlpatterns = [
    path('list_filmes/',list_filmes, name='list_filmes'),
    path('new_filmes/', new_filmes, name='new_filmes')

]