from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .models import Profile, FriendRequest
from albums.models import Album
from .forms import ProfileModelForm, EmailInviteForm
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags

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
    print(friends)
    family = profile.relations.all()
    print(family)

    
    template = 'profiles/profile_detail.html'
    context = {
        'profile': profile,
        'friends': friends,
        'family': family,
        'albums': albums,
        'plc_albums': plc_albums,
        'pvt_albums': pvt_albums,
    }
    
    return render(request, template, context)


# TODO add logic for buttons
def find_friends(request):
    """
    Create a find_list to suggest 'People you may know' of the current users friends friends. Only add them if they haven't already been added. Exclude existing friends profiles and the current user's profile. 
    """
    find_list = [] # consider changing to set() if time
    sent_requests = set()
    rec_requests = set()
    sent_f_requests = FriendRequest.objects.filter(
        from_user=request.user
    )
    rec_f_requests = FriendRequest.objects.filter(
        to_user=request.user
    )
    print(rec_requests)
    me = request.user
    my_friends = me.profile.friends.all()
    profiles = Profile.objects.exclude(
        user=request.user
    )
    for user in profiles:
        user_friends = user.friends.all()
        for friend in user_friends:
            if friend not in find_list and friend != me:
                if friend not in my_friends:
                    find_list.append(friend)         

    for sent in sent_f_requests:
        print('Sent', sent)
        sent_requests.add(sent)
    
    
    for rec in rec_f_requests:
        print('Rec', rec)
        rec_requests.add(rec)
    
    template = 'profiles/find_friends.html'
    context = {
        'find_list': find_list,
        'sent': sent_requests,
        'rec': rec_requests,
    }

    return render(request, template, context)

def send_request(request, id):
    user = get_object_or_404(User, id=id)
    print(profile)
    f_request, created = FriendRequest.objects.get_or_create(
        from_user=request.user,
        to_user=user
    )
    messages.success(
        request,
        f'Your friend request to {user} has been sent.'
    )
    
    return redirect('/profiles/%s/' % user.profile.slug)

def cancel_request(request, id):
    user = get_object_or_404(User, id=id)
    f_request = FriendRequest.objects.filter(
        from_user=request.user,
        to_user=user
    )
    f_request.delete()
    messages.success(
        request, 
        f'Your friend request to {user} has been cancelled.'
    )
    
    return redirect('/profiles/%s/' % user.profile.slug)

def delete_request(request, slug):
    from_user = get_object_or_404(Profile, slug=slug)
    f_request = FriendRequest.objects.filter(
        from_user=from_user,
        to_user=request.user
    )
    f_request.delete()
    messages.success(
        request, 
        f'Your friend request from {from_user} has been removed.'
    )
    return redirect('/profiles/%s/' % request.user.profile.slug)


def accept_request(request, slug):
    from_user = get_object_or_404(Profile, slug=slug)
    f_request = FriendRequest.objects.filter(
        from_user=from_user,
        to_user=request.user
    )
    # TODO logic to accept request, add to friends and delete request
    messages.succes(request, 'You are now friends with {from_user}')
    return redirect('/profiles/%s/' % request.user.profile.slug)


def search_profiles(request):
    query = request.GET.get('q')
    results = Profile.objects.filter(user__username__icontains=query)
    template = 'profiles/search_profiles.html'
    context = {
        'results': results,
        'query': query
    }

    return render(request, template, context)

# TODO try to work out how to keep track of email sent by the user not important
def email_invite(request):
    if request.method == 'POST':
        form = EmailInviteForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = f'{cd["name"]}'
            subject = f'{cd["name"]} has sent you a invitation'
            from_email = settings.DEFAULT_FROM_EMAIL
            to = [f'{cd["to"]}']
            comment = f'{cd["comment"]}'
            html_template = get_template('profiles/email/email_invite_message.html').render()
            msg = EmailMultiAlternatives(subject=subject, comment=comment, from_email=from_email,to=[cd['to']])
            msg.attach_alternative(html_template, 'text/html')
            msg.send(fail_silently=False)
            messages.success(request, 'Your email has been sent')
            return HttpResponseRedirect(reverse('profiles:find_friends'))
    else:
         form = EmailInviteForm()
    
    template = 'profiles/email_invite.html'
    context = {
        'form': form,
    }
    return render(request, template, context)