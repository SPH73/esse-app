from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse, redirect, resolve_url
from profiles.models import Profile
from django.template.defaultfilters import slugify
from utils.slug import get_slug_suffix
from taggit.managers import TaggableManager


class Album(models.Model):
    title = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name='albums', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
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
    
    def get_assets(self):
        return self.assets.all()
    
    def get_thumb(self):
        return self.assets.last()
    
    def get_slug(self):
        return self.slug
    
    def get_asset_count(self):
        return self.assets.all().count()
       
    def get_absolute_url(self):
        return reverse('albums:album_detail', args=[self.slug])
    

def album_media_dir(instance, filename):
    return f'Esse/user_uploads/albums/user_{instance.profile}/{instance.album.slug}/{filename}'


class Asset(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='assets')
    media = models.FileField(upload_to=album_media_dir)
    added = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    slug = slug = models.SlugField(unique=True, blank=True)
    tags = TaggableManager()
    
    def save(self, *args, **kwargs):
        """
        Auto generate the slug using the title and album and append a random suffix
        """
        suffix = get_slug_suffix()
        add_slug = slugify(f'{self.title}-{self.album}-{suffix}')
        self.slug = add_slug
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.slug