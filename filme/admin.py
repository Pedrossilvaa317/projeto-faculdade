from django.contrib import admin
from .models import Filmes
from .models import Generos


class FilmeAdmin(admin.ModelAdmin):
    list_display = ['filme', 'genero', 'quantidade','preco']
    ordering = ['-filme']
    search_fields = ['filme']
    list_filter = ['genero']
    list_editable = ['quantidade', 'preco']

admin.site.register(Filmes, FilmeAdmin)
admin.site.register(Generos)
