from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('find-friends/', views.find_friends, name='find_friends'),
    path('search-profiles/', views.search_profiles, name='search_profiles'),
]
