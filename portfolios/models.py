import uuid
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

User = get_user_model()

class Portfolio(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    name = models.CharField(help_text='Give your portfolio a relevant name. ', max_length=50)
    slug = models.SlugField(max_length=150, unique_for_date='created')
    description = models.TextField('Portfolio description')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField('last updated', auto_now=True, null=True)
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('portfolios:portfolio_detail',
                       args=[self.created.year,
                             self.created.month,
                             self.created.day,
                             self.slug])


class Bucket(models.Model):
    PRIVATE = 'PVT'
    SHARED = 'SHR'
    PUBLIC = 'PBL'
    BUCKET_PRIVACY_CHOICES = [
        (PRIVATE, 'Private'),
        (SHARED, 'Shared'),
        (PUBLIC, 'Public')
    
]
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='buckets')
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique_for_date='created')
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField('Last Updated', auto_now=True)
    access_list = ArrayField(models.EmailField(max_length=50, blank=True), size=8, null=True, blank=True, help_text="Comma separated list of up to 8 email addresses that you want to share this bucket with. Not used on public buckets.")
    make_public = models.BooleanField(default=False)
     
    class Meta:
        ordering = ('-created',)
         
    def __str__(self):
        return self.name
        
    # def get_absolute_url(self):
    #     return reverse('bucket_detail', args=[str(self.id)])