from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Profile, FriendRequest
from albums.models import Album
from .forms import ProfileModelForm
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

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
    # need to put in a check if request.user is friend or family to view albums
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
    me = request.user
    my_friends = me.profile.friends.all()
    # sent_request =[]
    profiles = Profile.objects.exclude(user=request.user)
    for user in profiles:
        user_friends = user.friends.all()
        for friend in user_friends:
            if friend not in find_list and friend != me:
                if friend not in my_friends:
                    find_list.append(friend)         

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

def send_request(request, slug):
    profile = get_object_or_404(profile, slug=slug)
    f_request, created = FriendRequest.objects.get_or_create(
        from_user=request.user,
        to_user=profile
    )
    return HttpResponseRedirect('/profiles/{profile.slug}')

def friend_requests(request):
    sent_f_requests = FriendRequest.objects.filter(from_user=request.user)
    rec_f_requests = FriendRequest.objects.filter(to_user=profile.slug)

    template = ''
    context = {
        'sent_f_requests': sent_f_requests,
        'rec_f_requests': rec_f_requests,
    }

    return render('profiles/profile.html')

def accept_request(request, slug):
    from_user = get_object_or_404(Profile, slug=slug)
    f_request = FriendRequest.objects.filter(from_user=from_user, to_user=request.user)
    
