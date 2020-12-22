from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
# import stripe

# stripe.api_key = settings.STRIPE_TEST_PUBLISHABLE_KEY

# def donate(request):
#     template = 'donations/donate.html'
#     return render(request, template)

# def charge(request):
#     amount = 500
#     if request.method == 'POST':
#         stripe.Charge.create(
#             amount=amount,
#             currency="gbp",
#             source="tok_visa",
#             description="Donation",
#         )
#         stripe.Customer.create(
#             email=request.user.eamil,
#             username=request.user,
#             description="Donation from platform user",
#         )
        
#         stripe.Charge.capture(
#             "ch_1I1FkxL0aOfkg477x5ZP5VPn",
#         )
        
#         charge = stripe.Charge.retrieve(
#             "ch_1I1DYxL0aOfkg477BMEE1Lie",
#             api_key=stripe.api.key
#         )
#         charge.save() # Uses the same API Key.
        
#         stripe.Customer.retrieve(
#             "cus_IcUkTDxkGdUi4m"
#         )
        
#         print('Data:', request.POST, request.user, request.user.email)
#     return redirect(reverse('donations:success', args=[amount]))

# def success(request, args):
#     amount = args 
#     context = {
#         'amount': amount
#     }
    
#     template = 'donations/success.html'
#     return render(request, template, context)

