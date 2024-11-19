from django.urls import path
from .views import register, CustomLoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profil', views.profil, name='profil'),
]
