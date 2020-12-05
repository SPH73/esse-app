from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib import messages
from .models import Profile
from albums.models import Album
from .forms import ProfileModelForm


def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST':
        form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            
    form = ProfileModelForm(instance=profile)
    albums = profile.albums.all()
    plc_albums = albums.exclude(is_public=False)
    pvt_albums = albums.exclude(is_public=True)
   
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form':form,
        'albums': albums,
        'plc_albums': plc_albums,
        'pvt_albums': pvt_albums,
    }
    
    return render(request, template, context)
