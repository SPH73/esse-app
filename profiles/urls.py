from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('find-friends/', views.find_friends, name='find_friends'),
    path('email-invite/', views.email_invite, name='email-invite'),
    path('search-result/', views.search_profiles, name='search_result'),
    path('<slug:slug>/', views.user_detail, name='user_detail'),
    path('friend-request/send/<uuid:id>', views.send_request, name='send_request'),

]
