from django.db import models
from django.contrib.auth import get_user_model
from profiles.models import Profile

class Album(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-updated',)
        
    abstract = True


class Private(Album):
    is_public = models.BooleanField(default=False)
    profile = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, related_name='private_albums', blank=True, null=True
    )
    
    class Meta:
        verbose_name_plural = 'Private Albums'

    def __str__(self):
        return f"{self.title} - {self.profile}"


class Public(Album):
    is_public = models.BooleanField(default=True)
    profile = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, related_name='public_albums', blank=True, null=True
    )
    class Meta:
        verbose_name_plural = 'Public Albums'

    def __str__(self):
        return f"{self.title} - {self.profile}"
