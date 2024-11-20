from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .models import Article
from django.contrib.auth.views import LoginView
from .models import MovieSelection
from .forms import MovieSelectionForm




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


def profile(request):
    #Vérification si l'utilisateur est connecté 
    if not request.user.is_authenticated :
        return render(request, 'home.html')
    
    selections = MovieSelection.objects.filter(user=request.user)
    return render(request, 'profile.html', {'selections': selections})

    

def select_movie(request):
    if request.method == 'POST':
        form = MovieSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user  # Associe l'utilisateur connecté
            selection.save()
            return redirect('profile')  # Redirige vers la page profil
    else:
        form = MovieSelectionForm()
    return render(request, 'select_movie.html', {'form': form})


def deconnexion(request):
    logout(request)
    return redirect('home')



