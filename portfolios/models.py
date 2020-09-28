import uuid
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse



User = get_user_model()

class Portfolio(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name


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
    slug = models.SlugField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateTimeField('Last Updated', auto_now=True)
    privacy = models.CharField('Type', max_length=10, choices=BUCKET_PRIVACY_CHOICES, default=PRIVATE)
    whitelist = models.BooleanField(default=False)
    members = ArrayField(models.EmailField(max_length=50, blank=True), size=8, null=True, blank=True)
     
     
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('bucket_detail', kwargs={'slug':str(self.slug)})