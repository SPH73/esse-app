from django.urls import path
from . import views


app_name = 'donations'
urlpatterns = [
    path('', views.donate, name='donations'),
    path('charge/', views.charge, name='charge'),
    path('success/<str:args>/', views.success, name='success' )
]