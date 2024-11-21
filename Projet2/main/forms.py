from django import forms
from .models import MovieSelection, Movie, Horaire

class MovieSelectionForm(forms.ModelForm):
    movie_name = forms.ModelChoiceField(
        queryset=Movie.objects.all(),
        empty_label="Choisissez un film",
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'movie-select'}),
        label="Film"
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ajouter un attribut `data-price` pour chaque option
        self.fields['movie_name'].widget.choices = [
            (movie.id, f"{movie.name} - {movie.ticket_price}€") 
            for movie in self.fields['movie_name'].queryset
        ]

    horaire = forms.ModelChoiceField(
        queryset=Horaire.objects.all(),
        empty_label="Choisissez un horaire",
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Horaire"
    )

    class Meta:
        model = MovieSelection
        fields = ['movie_name', 'tickets', 'horaire']
        widgets = {
            'tickets': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de billets',
                'id': 'ticket-count',
            }),
        }