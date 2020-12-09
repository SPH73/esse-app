from django.urls import path
from . import views

app_name = 'albums'
urlpatterns = [
    path('gallery', views.gallery, name='gallery'),
    path('album-detail/<str:slug>', views.album_detail, name='album-detail'),
    path('upload', views.upload, name='media-upload'),
]