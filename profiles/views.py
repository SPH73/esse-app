from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Profile
from albums.models import Album, Private, Public
from .forms import ProfileModelForm


def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST':
        form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            
    form = ProfileModelForm(instance=profile)
    public_albums = profile.public_albums.all()
    private_albums = profile.private_albums.all()
    
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form':form,
        'private_albums': private_albums,
        'public_albums': public_albums
    }
    
    return render(request, template, context)
