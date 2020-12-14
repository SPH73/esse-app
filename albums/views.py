from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django import forms
from .models import Album, Asset
from profiles.models import Profile
from .forms import AssetModelForm, CreateAlbumModelForm

def gallery(request):
    """
    Render a view to create and display a gallery of users albums
    """
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
        'album_form': album_form,
    }
    return render(request, template, context)
   
def album_detail(request, album):
    """
    Get the authenticated user profile to generate the cloud storage folder if not already created, use the profile related name to retieve and display the assets stored in a single album, render a form and add the chosen asset to the album.
    """
    profile = get_object_or_404(Profile, user=request.user)
    albums = profile.albums.all()
    album = albums.get(slug=album)
    assets = album.assets.all()
    featured = album.assets.order_by('-added')
    display = album.assets.all()
    if request.method == 'POST':
        asset_form = AssetModelForm(request.POST, request.FILES)
        if asset_form.is_valid():
            asset = asset_form.save(commit=False)
            asset.album = album
            asset.profile = profile
            asset.save()
            messages.success(request, 'Media added successfully')
        else:
            messages.error(request, 'Error adding your media')
    else:
        asset_form = AssetModelForm()
    template = 'albums/album_detail.html'    
    context = {
        'profile': profile,
        'albums': albums,
        'album': album, 
        'assets': assets,
        'display': display,
        'featured': featured,
        'asset_form': asset_form}
    return render(request, template, context)

def asset_detail(request):
    pass

def album_delete_view(request, album):
    profile = get_object_or_404(Profile, user=request.user)
    albums = profile.albums.all()
    album = albums.get(slug=album)      
    
    if request.method == "POST": 
        album.delete()
    
    template = 'album/gallery.html'
    context = {
        'album':album,
    }
    
    return render(request, template, context) 

def asset_delete_view(request, asset): 
    asset = get_object_or_404(Asset, slug=asset) 
    
    template = 'album/detail_view.html'
    context = {
        'asset':asset
    }
    
    if request.method == "POST":
        asset.delete()
    
    return render(request, template, context) 
