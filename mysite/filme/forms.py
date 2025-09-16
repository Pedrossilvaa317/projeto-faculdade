from django.forms import ModelForm
from .models import Filmes

class FilmesForm(ModelForm): #usar palavras arbitratios (o nome da class junto com forms)
    class Meta:
        model = Filmes
        fields = '__all__'