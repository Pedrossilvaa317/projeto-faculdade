from django.shortcuts import render, redirect
from .models import Filmes
from .forms import FilmesForm

def list_filmes(request):
    filmes = Filmes.objects.all()#retorna um querySet que é uma lista de objetos e tambem instacia filmes
    template_name = 'list_filmes.html'
    context = {
        'filmes' : filmes
    }
    return render (request, template_name,context)

def new_filmes(request):
    if request.method == 'POST': # se veio do metodo post é pq veio do form
        form = FilmesForm(request.POST) #request.post é a lista dos campos do que veio no forms
        if form.is_valid():
            form.save()
            return redirect('filme:list_filmes')# após salvar retorna ao filmes atraves do caminho, por conta do redirect
    else:
        template_name = 'new_filmes.html'
        context = {
            'mensagem':'Cadastro de filmes',
            'form':FilmesForm()
        }
        return render(request, template_name, context)#render juntar o html com o conteudo
    
def update_filmes(request,pk):
    filme = Filmes.objects.get(id = pk)
    if request.method == 'POST': 
        form = FilmesForm(request.POST,instance = filme) 
        if form.is_valid():
            form.save()
            return redirect('filme:list_filmes')# após salvar retorna ao filmes atraves do caminho, por conta do redirect
    else:
        template_name = 'update_filmes.html'
        context = {
            'mensagem':'Alteração de filmes',
            'form':FilmesForm(instance = filme),
            'pk':pk
        }
        return render(request, template_name, context)#render juntar o html com o conteudo
    
def delete_filmes(request,pk):
    filme = Filmes.objects.get(id = pk)
    filme.delete()
    
    return redirect('filme:list_filmes')
    
    