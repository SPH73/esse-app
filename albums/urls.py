from django.urls import path
from . import views

app_name = 'albums'
urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<slug:album>', views.album_detail, name='album_detail'),
]