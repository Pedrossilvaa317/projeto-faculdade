from django.shortcuts import render
from .models import Filmes

def list_filmes(request):
    filmes = Filmes.objects.all()
    template_name = 'list_filmes.html'
    context = {
        'filmes' : filmes
    }
    return render (request, template_name,context)