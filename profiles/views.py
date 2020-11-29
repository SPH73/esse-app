from django.shortcuts import render

from . import views

def profile(request):
    template = 'profiles/profile.html'
    context = {}
    
    return render(request, template, context)
