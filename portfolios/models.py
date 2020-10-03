
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
    name = models.CharField('Give your portfolio a name', max_length=50)
    slug = models.SlugField(max_length=150, unique_for_date='created_on')
    description = models.TextField('Portfolio description')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField('last updated', auto_now=True, null=True)
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('portfolio_detail', args=[str(self.id)])


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
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique_for_date='created')
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField('Last Updated', auto_now=True)
    access_list = ArrayField(models.EmailField(max_length=50, blank=True), size=8, null=True, blank=True)
    make_public = models.BooleanField(default=False)
     
    class Meta:
        ordering = ('-created',)
         
    def __str__(self):
        return self.name
    
    def save(self):
        self.user = self.request.user 
        self.slug = '%s%s' % (slugify(self.user.username), slugify(self.name))
        super(Portfolio, self).save()
    
    def get_absolute_url(self):
        return reverse('bucket_detail', args=[str(self.id)])