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
    album = get_object_or_404(Album, slug=album)
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
        'album': album, 
        'display': display,
        'asset_form': asset_form}
    return render(request, template, context)


def album_delete(request, album):
    """
    Find and delete the album instance and all related assets from the database.
    """
    profile = get_object_or_404(Profile, user=request.user)
    album = get_object_or_404(Album, slug=album) 
    template = 'albums/gallery.html'
    context = {
        'album':album,
    }
    
    if request.method == "POST":
        if not profile:
            messages.warning(request, "This album belongs to another profile, you cannot delete it.")
            return redirect('home')
        
        album.delete()
        messages.success(request, "Album deleted")
        
    return render(request, template, context) 


def asset_detail(request, album, asset):
    """
    Get the asset from the album
    """
    album = get_object_or_404(Album, slug=album) 
    asset = get_object_or_404(Asset, slug=asset)
    template = 'albums/asset_detail.html'    
    context = {
        'album':album,
        'asset': asset
        }
    
    return render(request, template, context)


def asset_delete(request, album, asset): 
    profile = get_object_or_404(Profile, user=request.user)
    album = get_object_or_404(Album, slug=album)
    asset = get_object_or_404(Asset, slug=asset)
    template = 'albums/asset_detail.html'
    context = {
        'album': album,
        'asset':asset,
        'profile': profile
    }
    
    if request.method == "POST":
        if not profile:
            messages.warning(request, "This album belongs to another profile, you cannot delete it's assets.")
            return redirect('home')
        
        asset.delete()
        messages.success(request, "Asset deleted successfully")
        
        return render(request, 'albums/album_detail.html')
    
    return render(request, template, context)

def user_album(request, album):
    # need to put in a check if request.user is friend or family to view albums
    album = get_object_or_404(Album, slug=album)
    profile = album.get_album_profile()
    
    assets = album.assets.all()
  
    template = 'albums/user_album.html'
    context = {
        'album': album,
        'assets': assets,
        'profile': profile
    }
    
    return render(request, template, context)

def album_asset(request, album, asset):
    """
    Get the asset from the album
    """
    album = get_object_or_404(Album, slug=album) 
    asset = get_object_or_404(Asset, slug=asset)
    template = 'albums/album_asset.html'    
    context = {
        'album':album,
        'asset': asset
        }
    
    return render(request, template, context)
