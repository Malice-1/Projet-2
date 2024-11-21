from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Movie(models.Model):
    name = models.CharField(max_length=255)
    ticket_price = models.DecimalField(max_digits=5, decimal_places=2,default=10)

    def __str__(self):
        return f"{self.name} - {self.ticket_price}€"

class Horaire(models.Model):
    name = models.CharField(max_length=8, default="17h30")

    def __str__(self):
        return self.name

class MovieSelection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)  # Relation avec Movie
    tickets = models.PositiveIntegerField()
    horaire = models.ForeignKey(Horaire, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)  # Calculé automatiquement
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Récupérer le ticket_price depuis l'objet Movie lié
        if self.movie_name:
            self.total_price = self.tickets * self.movie_name.ticket_price
        super().save(*args, **kwargs)