from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
import stripe

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


def donate(request):    
    template = 'donations/donate.html'
    stripe_key = settings.STRIPE_TEST_PUBLISHABLE_KEY
    context = {
        'stripe_key':stripe_key
    }
    return render(request, template, context)

def charge(request):
    amount = 5
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=amount*100,
            currency='gbp',
            description='donation',
            source=request.POST['stripeToken']
        )
        print('Data: ', request.POST)
    return redirect(reverse('donations:success', args=[amount]))

def success(request, args):
    username = request.user.username
    email = request.user.email
    
    context = {
        'amount': args,
        'username': username
    }
    template = 'donations/success.html'
    return render(request, template, context)

