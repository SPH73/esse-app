from django.shortcuts import render, get_object_or_404
from .models import Portfolio, Bucket
from django.contrib.auth import get_user_model
from .forms import BucketForm
def portfolio_list(request, user):
    portfolios = Portfolio.objects.all()
    user = get_user_model()
    context = {'portfolios':portfolios, 'user':user}
    return render(request, 'portfolios/portfolio_list.html', context)

def portfolio_detail(request, year, month, day, portfolio):
    portfolio = get_object_or_404(Portfolio, 
                                  slug=portfolio,
                                  updated__year=year,
                                  updated__month=month,
                                  updated__day=day)
    buckets = portfolio.buckets.all()
    new_bucket = None
    if request.method == 'POST':
        bucket_form = BucketForm(data=request.POST)
        if bucket_form.is_valid():
            new_bucket = bucket_form.save(commit=False)
            new_bucket.portfolio = portfolio
            new_bucket.save()
        else:
            bucket_form = BucketForm()        
    context = {'portfolio': portfolio, 'buckets': buckets, 'new_bucket':new_bucket, 'bucket_form': bucket_form}
    return render(request, 'portfolios/portfolio_detail.html', context)

