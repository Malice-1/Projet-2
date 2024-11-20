from django import forms
from .models import MovieSelection, Movie

class MovieSelectionForm(forms.ModelForm):
    movie_name = forms.ModelChoiceField(
        queryset=Movie.objects.all(),
        empty_label="Choisissez un film",
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Film"
    )

    class Meta:
        model = MovieSelection
        fields = ['movie_name', 'tickets', 'time']
        widgets = {
            'tickets': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de billets'}),
            'time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Horaire'}),
        }