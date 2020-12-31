from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect,render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f'{cd["subject"]}'
            from_email = f'{cd["from_email"]}'
            message = f'{cd["message"]}'
            try:
                send_mail(subject, message, from_email, ['esse@pixpimedia.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            messages.success(request, 'Thank you for contacting us. Our usual response time is within 24 hours')
            return redirect('home')
    form = ContactForm()
    template = 'contact.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
