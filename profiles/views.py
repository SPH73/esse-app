from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .models import Profile, FriendRequest
from albums.models import Album
from .forms import ProfileModelForm, EmailInviteForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags
from profiles.forms import UserEditForm

User = get_user_model()

   
def user_edit(request):
    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(data=request.POST, user=request.user)
        if edit_form.is_valid() and password_form.is_valid():
            edit_form.save()
            password_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profiles:profile')
        return redirect('profiles:update')
    
    edit_form = UserEditForm(instance=request.user)
    password_form = PasswordChangeForm(user=request.user)
    
    context = {
        'edit_form': edit_form,
        'password_form': password_form,
    }
    template = 'profiles/update.html'
    return render(request, template, context)
    
def profile(request):
    #TODO ADD IN ACCOUNT UPDATE FORM TO THIS VIEW
    """
    A view for the request users profile with edit profile form
    """
    profile = get_object_or_404(Profile, user=request.user)
    albums = profile.albums.all()
    plc_albums = albums.exclude(is_public=False)
    pvt_albums = albums.exclude(is_public=True)
    sent_f_requests = FriendRequest.objects.filter(
        from_user=profile.user
    )
    rec_f_requests = FriendRequest.objects.filter(
        to_user=profile.user
    )

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
        'sent_req': sent_f_requests,
        'rec_req': rec_f_requests,
    }

    return render(request, template, context)

def user_detail(request, slug):
    """
    Profile view of all users and if seen by profile owner then the view will seen from the persective of another user
    """
    user = request.user
    profile = Profile.objects.get(slug=slug)  
    albums = profile.albums.all()
    plc_albums = albums.exclude(is_public=False)
    pvt_albums = albums.exclude(is_public=True)
    
    friends = profile.friends.all()
    family = profile.relations.all()

    receiver = FriendRequest.objects.filter(from_user=profile.user)
    received_id = receiver.object.get(receiver_id=receiver.id)
    sender = FriendRequest.objects.filter(to_user=profile.user)
    
    received = []
    sent = []
    for item in receiver:
        received.append(item.to_user)
    for item in sender:
        sent.append(item.from_user)
        
    add_family = False
    if profile in request.user.profile.friends.all():
        add_family = True
        
    remove_family = False
    if profile in request.user.profile.relations.all():
        remove_family = True

    template = 'profiles/profile_detail.html'
    context = {
        'profile': profile,
        'friends': friends,
        'family': family,
        'albums': albums,
        'plc_albums': plc_albums,
        'pvt_albums': pvt_albums,
        'received': received,
        'sent': sent,
        'received_id': received_id,
        'add_family': add_family,
        'remove_family': remove_family,
    }
    
    return render(request, template, context)



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
   
    template = 'profiles/find_friends.html'
    context = {
        'find_list': find_list,
    }

    return render(request, template, context)

def friend_list(request):
    """
    Get the profile of the logged in user to access and render their list of friends
    """
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile,
    }
   
    return render(request, 'profiles/my_friends.html', context)

def family_list(request):
    """
    Get the profile of the logged in user to access and render their list of family
    """
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile,
    }
   
    return render(request, 'profiles/my_family.html', context)

def requests(request):
    """
    A view to display the logged in users friend requests
    """
    to_user=request.user
    profile = get_object_or_404(Profile, user=request.user)
    rec_f_requests = FriendRequest.objects.filter(
        to_user=profile.user
    )
    print('rec_f_requests: ',rec_f_requests)
   
    context = {
       'profile': profile,
       'rec_f_requests':rec_f_requests
    }
   
    return render(request, 'profiles/my_requests.html', context)

def send_request(request, id):
    """
    Send a friend request to users
    """
    user = get_object_or_404(User, id=id)
    f_request, created = FriendRequest.objects.get_or_create(
        from_user=request.user,
        to_user=user
    )
    if created:
        messages.success(
            request,
            f'Your friend request to {user} has been sent.'
        )
        
        return redirect('/profiles/%s/' % user.profile.slug)
    messages.info(request, f'You have already sent a friend request to {user}')
    return redirect('/profiles/%s/' % user.profile.slug)

def cancel_request(request, id):
    """
    Cancel a sent friend request
    """
    user = get_object_or_404(User, id=id)
    f_request = FriendRequest.objects.filter(
        from_user=request.user,
        to_user=user
    )
    f_request.delete()
    messages.success(
        request, 
        'Your friend request has been cancelled.'
    )

    return redirect('profiles:profile')

def delete_request(request, id):
    """
    Delete a received friend request
    """
    f_request = FriendRequest.objects.get(id=id)
    f_request.delete()
    messages.success(
        request, 
        f'Your friend request has been removed.'
    )
    return redirect('profiles:profile')


def accept_request(request, id):
    """
    Accept a friend request
    """
    f_request = FriendRequest.objects.get(id=id)
    if f_request.to_user == request.user:
        f_request.to_user.profile.friends.add(f_request.from_user)
        f_request.from_user.profile.friends.add(f_request.to_user)
        f_request.delete()
        messages.success(request, 'You are now friends with {f_request.from_user}')
    return redirect('profiles:my_friends')


def search_profiles(request):
    """
    Search form to query usernames
    """
    query = request.GET.get('q')
    results = Profile.objects.filter(user__username__icontains=query)
    template = 'profiles/search_profiles.html'
    context = {
        'results': results,
        'query': query
    }

    return render(request, template, context)

def email_invite(request):
    """
    Form to collect email address to send an email invite with link to sign up
    """
    if request.method == 'POST':
        form = EmailInviteForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = f'{cd["name"]}'
            subject = f'{cd["name"]} has sent you a invitation'
            from_email = settings.DEFAULT_FROM_EMAIL
            comment = f'{cd["comment"]}'
            html_template = get_template('profiles/email/email_invite_message.html').render()
            msg = EmailMultiAlternatives(subject, comment, from_email, [cd['to']])
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