from django.urls import path
from . import views

app_name = 'albums'
urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<slug:album>/', views.album_detail, name='album_detail'),
    path('<slug:album>/delete/', views.album_delete, name='delete_album'),
    path('<slug:album>/<slug:asset>/', views.asset_detail, name='asset_detail'),
    path('<slug:album>/<slug:asset>/delete/', views.asset_delete, name='delete_asset'),
]