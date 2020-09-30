from  django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView)

from .models import Portfolio, Bucket

class PortfolioCreateView(CreateView):
    model = Portfolio
    fields = ['name', 'description']
    success_url = 'portfolio_list'
    
    def post(self, request, *args, **kwargs):
        portfolio_form = PortfolioCreateView(request.POST)
        if portfolio_form.is_valid():
            portfolio = Portfolio(
            owner=request.user,
            name=portfolio_form.cleaned_data['name']
            )
            portfolio.save()
        else:
            raise Exception
        return redirect(reverse_lazy('portfolio_detail', args=[self.get_object().id]))
    
class PortfolioListView(ListView):
    model = Portfolio
    context_object_name = 'portfolio_list'


class BucketCreateView(CreateView):
    model = Bucket
    fields = '__all__'
    success_url = 'bucket_list'

class BucketListView(ListView):
    model = Bucket
    context_object_name = 'bucket_list'
    
class PortfolioDetailView(DetailView):
    model = Portfolio
            
    def get_context_data(self, *args,  **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['bucket_list'] = BucketListView()
        return context

class BucketDetailView(DetailView):
    model = Bucket
   

class PortfolioUpdateView(UpdateView):
    fields = ['name']
    success_url = 'portfolio_detail'
    
    
class PortfolioDeleteView(DeleteView):
    model = Portfolio
    success_url = 'portfolio_list'

   
class BucketUpdateView(UpdateView):
    fields = '__all__'
    success_url = 'bucket_detail.html'
    
        
class BucketDeleteView(DeleteView):
    model = Bucket
    success_url = 'bucket_list.html'
    

