from django.contrib import admin
from .models import Album, Asset


class AlbumModelAdmin(admin.ModelAdmin):
    list_display = (
        'profile',
        'id',
        'slug',
        'created',
        'updated',
        'is_public',
    )
    ordering = ('-updated',)


class AssetModelAdmin(admin.ModelAdmin):
    list_display = (
        'album',
        'title',
        'media',
        'slug',
        'added',
    )
    ordering = ('-added',)

admin.site.register(Album, AlbumModelAdmin)
admin.site.register(Asset, AssetModelAdmin)
