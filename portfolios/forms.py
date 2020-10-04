from django.forms import ModelForm

from .models import Portfolio, Bucket

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name', 'description']

class BucketForm(ModelForm):
    class Meta:
        model = Bucket
        fields = ['name', 'access_list', 'make_public']