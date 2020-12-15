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
   Get the user profile to retrieve all related albums and list the assets and generate a form to add assets.
    """
    profile = get_object_or_404(Profile, user=request.user)
    albums = profile.albums.all()
    print('Albums: ', albums)
    album = albums.get(slug=album)
    print('Album: ', album)
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
        'display': display,
        'asset_form': asset_form}
    return render(request, template, context)

def album_delete(request, album):
    """
    Find and delete the album instance and all related assets from the database.
    """
    profile = get_object_or_404(Profile, user=request.user)
    albums = profile.albums.all()
    album = get_object_or_404(Album, slug=album) 
    template = 'albums/gallery.html'
    context = {
        'album':album,
        'albums':albums,
    }
    
    if request.method == "POST": 
        album.delete()
        messages.success(request, "Album deleted")
        
    return render(request, template, context) 

def asset_detail(request, album, asset):
    """
    Get the asset from the album
    """
    album = get_object_or_404(slug=album)
    asset = album.asset.get(slug=asset)

    template = 'albums/album_detail.html'    
    context = {
        'album':album,
        'asset': asset
        }
    
    return render(request, template, context)


# def asset_delete(request, album, asset): 
#     profile = get_object_or_404(Profile, user=request.user)
#     albums = profile.albums.all()
#     album = albums.get(slug=album)
#     assets = album.assets.all()
#     asset = assets.get(slug=asset)
#     template = 'albums/asset_view.html'
#     context = {
#         'asset':asset,
#         'album':album,
#     }
    
#     if request.method == "POST":
#         asset.delete()
    
#     return render(request, template, context) 
