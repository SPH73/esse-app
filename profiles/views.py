from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Profile, FriendRequest
from albums.models import Album
from .forms import ProfileModelForm
from django.contrib.auth import get_user_model

User = get_user_model()


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

def user_detail(request, slug):
    # need to put in a check if request.user is friend or family to  view albums
    profile = Profile.objects.get(slug=slug)
    albums = profile.albums.all()
    plc_albums = albums.exclude(is_public=False)
    pvt_albums = albums.exclude(is_public=True)
    friends = profile.friends.all()

    
    template = 'profiles/profile_detail.html'
    context = {
        'profile': profile,
    }
    
    return render(request, template, context)

def find_friends(request):
    """
    Create a find_list to suggest 'People you may know' of the current users friends friends. Only add them if they haven't already been added. Exclude existing friends profiles and the current user's profile. 
    """
    find_list = []
    profiles = Profile.objects.exclude(user=request.user)

    for profile in profiles:
        friends = profile.friends.all()
        for friend in friends:
            if friend in find_list:
                find_list = friends.exclude(profile=friend.profile)
            find_list+=friend
            
    ex_friends = request.user.profile.friends.all()
    
    for profile in ex_friends:
        if profile in find_list:
            find_list.remove(profile)
    if request.user.profile in find_list:
        find_list.remove(request.user.profile)

    template = 'profiles/find_friends.html'
    context = {
        'find_list': find_list,
    }

    return render(request, template, context)

def search_profiles(request):
    query = request.GET.get('q')
    results = Profile.objects.filter(user__username__icontains=query)
    template = 'profiles/search_profiles.html'
    context = {
        'results': results,
        'query': query
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
