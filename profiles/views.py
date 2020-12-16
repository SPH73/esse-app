from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Profile, FriendRequest
from albums.models import Album
from .forms import ProfileModelForm


def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    albums = profile.albums.all()
    plc_albums = albums.exclude(is_public=False)
    pvt_albums = albums.exclude(is_public=True)


    if request.method == 'POST':
        form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")

    form = ProfileModelForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form':form,
        'albums': albums,
        'plc_albums': plc_albums,
        'pvt_albums': pvt_albums,

    }

    return render(request, template, context)

def all_profiles(request):
    """
    Create a find_list of the current users friends friends. Only add them if they haven't already been added.
    """
    find_list = []
    profiles = Profile.objects.exclude(user=request.user)

    for profile in profiles:
        friends = profile.friends.all()
        for friend in friends:
            if friend in find_list:
                find_list = friends.exclude(profile=friend.profile)
            find_list+=friend
            
    template = 'profiles/all_profiles.html'
    context = {
        'find_list': find_list,
    }

    return render(request, template, context)

def search(request):
    users = Profile.objects.exclude(user=request.user)

    template = 'profiles/search.html'
    context = {
        'users':users,
    }

    return render(request, template, context)

def friend_requests(request):
    sent_f_requests = FriendRequest.objects.filter(from_user=profile)
    rec_f_requests = FriendRequest.objects.filter(to_user=profile)

    template = ''
    context = {
        'sent_f_requests': sent_f_requests,
        'rec_f_requests': rec_f_requests,
    }

    return render('profiles/friend_request.html')
