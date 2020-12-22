from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
import stripe

stripe.api_key = settings.STRIPE_TEST_PUBLISHABLE_KEY

def donate(request):
    template = 'donations/donate.html'
    return render(request, template)

def charge(request):
    amount = 5
    if request.method == 'POST':
        print('Data:', request.POST)
    return redirect(reverse('donations:success', args=[amount]))

def success(request, args):
    amount = args 
    context = {
        'amount': amount
    }
    
    template = 'donations/success.html'
    return render(request, template, context)

