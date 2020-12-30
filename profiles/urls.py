from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('my-profile/', views.profile, name='profile'),
    path('update/', views.user_edit, name='update'),
    path('my-friends/', views.friend_list, name='my_friends'),
    path('my-family/', views.family_list, name='my_family'),
    path('my-requests/', views.requests, name='my_requests'),
    path('email-invite/', views.email_invite, name='email_invite'),
    path('find-friends/', views.find_friends, name='find_friends'),
    path('search-result/', views.search_profiles, name='search_result'),
    path('<slug:slug>/', views.user_detail, name='user_detail'),
    path('friend-request/send/<uuid:id>/', views.send_request, name='send_request'),
    path('friend-request/cancel/<uuid:id>/', views.cancel_request, name='cancel_request'),
    path('friend-request/accept/<int:id>/', views.accept_request, name='accept_request'),
    path('friend-request/delete/<int:id>/', views.delete_request, name='delete_request'),
]
