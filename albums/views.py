from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django import forms
from .models import Album, Asset
from profiles.models import Profile
from .forms import AssetModelForm, CreateAlbumModelForm

def gallery(request):
    profile = get_object_or_404(Profile, user=request.user)
    albums = profile.albums.all()
    if request.method == 'POST':
        album_form = CreateAlbumModelForm(request.POST)
        if album_form.is_valid():
            album = album_form.save(commit=False)
            album.profile = profile
            album.save()
            messages.success(request, 'Album created successfully')
        else:
            messages.error(request, 'Error creating your album')
    else:
        album_form = CreateAlbumModelForm()
    
    template = 'albums/gallery.html'
    context = {
        'albums': albums,
        'album_form': album_form
    }
    return render(request, template, context)
   
def album_detail(request, album):
    profile = get_object_or_404(Profile, user=request.user)
    albums = profile.albums.all()
    album = albums.get(slug=album)
    assets = album.assets.all()
    asset = None
    if request.method == 'POST':
        asset_form = AssetModelForm(request.Post, request.FILES)
        if asset_form.is_valid():
            asset = asset_form.save(commit=False)
            asset.album = album
            asset.save()
            messages.success(request, 'Media added successfully')
        else:
            messages.error(request, 'Error adding your media')
    else:
        asset_form = AssetModelForm()
    template = 'albums/album_detail.html'    
    context = {'album': album, 
               'assets': assets, 
               'asset':asset, 
               'asset_form': asset_form}
    return render(request, template, context)

