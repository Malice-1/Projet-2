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
        return self.name

class MovieSelection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=255)
    ticket_price = models.DecimalField(max_digits=5, decimal_places=2,default=10)  # Prix par billet
    tickets = models.PositiveIntegerField()
    time = models.CharField(max_length=10)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)  # Calculé automatiquement
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calcul automatique du prix total
        self.total_price = self.tickets * self.ticket_price
        super().save(*args, **kwargs)
