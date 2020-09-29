from  django.urls import reverse_lazy

from django.views.generic import (
    FormView, UpdateView, DeleteView, ListView, DetailView)

from .forms import PortfolioForm, BucketForm
from .models import Portfolio, Bucket

class PortfolioCreateView(FormView):
    form_class = PortfolioForm
    template_name = 'portfolios/create_portfolio.html'
    success_url = 'portfolio_list'
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
        
class PortfolioListView(ListView):
    model = Portfolio
    context_object_name = 'portfolio_list'
    template_name = 'portfolios/portfolio_list.html'
    
class PortfolioDetailView(DetailView):
    model = Portfolio
    context_object_name = 'portfolio'
    template_name = 'portfolios/portfolio_detail.html'

class PortfolioUpdateView(UpdateView):
    fields = ['name']
    success_url = 'portfolio_detail'
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class PortfolioDeleteView(DeleteView):
    model = Portfolio
    success_url = 'portfolio_list'


class BucketCreateView(FormView):
    form_class = BucketForm
    template_name = 'portfolios/create_bucket.html'
    success_url = 'bucket_list'
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class BucketListView(ListView):
    model = Bucket
    context_object_name = 'buckets'
    template_name = 'portfolios/bucket_list.html'

class BucketDetailView(DetailView):
    model = Bucket
    context_object_name = 'bucket'
    template_name = 'portfolios/bucket_detail.html'
    
class BucketUpdateView(UpdateView):
    fields = [
        'name',
        'privacy',
        'members'
    ]
    success_url = 'bucket_detail.html'
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class BucketDeleteView(DeleteView):
    model = Bucket
    success_url = 'bucket_list.html'
    

