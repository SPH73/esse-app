from django.shortcuts import render, get_object_or_404
from .models import Portfolio, Bucket
from django.contrib.auth import get_user_model

def portfolio_list(request, user):
    portfolios = Portfolio.objects.all()
    user = get_user_model()
    context = {'portfolios':portfolios, 'user':user}
    return render(request, 'portfolios/list.html', context)

def portfolio_detail(request, year, month, day, portfolio):
    portfolio = get_object_or_404(Portfolio, 
                                  slug=portfolio,
                                  updated__year=year,
                                  updated__month=month,
                                  updated__day=day)
    context = {'portfolio': portfolio}
    return render(request, 'portfolios/detail.html', context)