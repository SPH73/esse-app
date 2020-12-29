from django.urls import path
from . import views

app_name = 'albums'
urlpatterns = [
    path('my-portfolio/', views.gallery, name='gallery'),
    path('user-albums/<slug:album>/', views.user_album, name='user_album'),
    path('user-albums/<slug:album>/<slug:asset>/', views.album_asset, name='album_asset'),
    path('my-portfolio/<slug:album>/', views.album_detail, name='album_detail'),
    path('my-portfolio/<slug:album>/delete/', views.album_delete, name='delete_album'),
    path('user-albums/<slug:album>/<slug:asset>/', views.asset_detail, name='asset_detail'),
    path('my-portfolio/<slug:album>/<slug:asset>/delete/', views.asset_delete, name='delete_asset'),
]