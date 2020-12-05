from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from profiles.models import Profile
from django.template.defaultfilters import slugify
from utils.slug import get_slug_suffix

class Album(models.Model):
    title = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name='albums', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('-updated',)
        constraints = [
            models.UniqueConstraint(fields=['title', 'profile'], name='unique_album')
        ]
        
    def save(self, *args, **kwargs):
        """
        Auto generate the slug using the title and profile and append a random suffix
        """
        suffix = get_slug_suffix()
        add_slug = slugify(f'{self.title}-{self.profile}-{suffix}')
        self.slug = add_slug
        super().save(*args, **kwargs)    

    def __str__(self):
        return self.slug
    
    def get_absolute_url(self):
        return reverse('album_detail', args=[self.title])