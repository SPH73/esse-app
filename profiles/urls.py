from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('users/', views.all_profiles, name='users'),
    path('search/', views.search, name='search'),
]
