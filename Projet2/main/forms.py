from django import forms
from .models import MovieSelection

class MovieSelectionForm(forms.ModelForm):
    class Meta:
        model = MovieSelection
        fields = ['movie_name', 'tickets', 'time', 'total_price']