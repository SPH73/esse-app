from django.contrib import admin
from .models import Album, MediaUploads

class AlbumModelAdmin(admin.ModelAdmin):
    list_display = (
        'profile',
        'slug',
        'created',
        'updated',
        'is_public',
    )
    ordering = ('-updated',)
    
admin.site.register(Album, AlbumModelAdmin)
admin.site.register(MediaUploads)

