from django.urls import path
from .views import register, CustomLoginView
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.deconnexion, name='logout'),
    path('profile', views.profile, name='profile'),
    path('select-movie/', views.select_movie, name='select_movie'),
]
