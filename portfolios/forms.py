from django.forms import ModelForm
from .models import Portfolio, Bucket

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name']
        
class BucketForm(ModelForm):
    class Meta:
        model = Bucket
        fields = ['name', 'privacy', 'members']
        
        def __init__(self, *args, **kwargs):
            super(BucketForm, self).__init__(*args, **kwargs)
            if self.instance.privacy == 'shared':
                    self.fields['whitelist'] = True
            else:
                self.fields['whitelist'] = False
                del self.instance.fields['members']
                    
                    
