from django.contrib import admin
from .models import Album, Private, Public

class PublicModelAdmin(admin.ModelAdmin):
    list_display = (
        'profile',
        'created',
        'updated',
    )
    ordering = ('-updated',)
    
class PrivateModelAdmin(admin.ModelAdmin):
    list_display = (
        'profile',
        'created',
        'updated',
    )
    ordering = ('-updated',)

admin.site.register(Private, PrivateModelAdmin)
admin.site.register(Public, PrivateModelAdmin)
