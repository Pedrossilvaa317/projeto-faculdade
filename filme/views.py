from django.shortcuts import render, redirect
from .models import Filmes
from .forms import FilmesForm

def list_filmes(request):
    filmes = Filmes.objects.all()
    template_name = 'list_filmes.html'
    context = {
        'filmes' : filmes
    }
    return render (request, template_name,context)

def new_filmes(request):
    print ('new_filmes', request.method)
    if request.method == 'POST':
        form = FilmesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filme:list_filmes')
    else:
        template_name = 'new_filmes.html'
        context = {
            'mensagem':'Cadastro de filmes',
            'form':FilmesForm()
        }
        return render(request, template_name, context)