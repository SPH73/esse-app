from django.urls import path
from . import views

app_name = 'albums'
urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<slug:album>/', views.album_detail, name='album_detail'),
    path('delete-album/<slug:album>/', views.album_delete_view, name='album_delete'),
    path('<slug:asset>/', views.asset_detail, name='asset_detail'),
    path('delete-asset/<slug:asset>/', views.asset_delete_view,name='asset_delete'),
]