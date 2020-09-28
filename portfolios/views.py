from django.views.generic import ListView, DetailView

from .models import Portfolio, Bucket

class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio_list.html'
    
class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'
    

class BucketListView(ListView):
    model = Bucket
    template_name = 'portfolio/bucket_list.html'
    
class PortfolioDetailView(DetailView):
    model = Bucket
    template_name = 'portfolio/bucket_detail.html'
