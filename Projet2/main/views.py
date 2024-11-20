from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Article
from django.contrib.auth.views import LoginView



def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte automatiquement l'utilisateur après l'inscription
            return redirect('home')  # Redirige vers la page d'accueil ou une autre page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



class CustomLoginView(LoginView):
    template_name = 'login.html'

def tiquets(request):
    return render(request, 'tiquets.html')