from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'avatar',
        'created',
        'updated',
    )
    ordering = ('-updated',)

admin.site.register(Profile, ProfileAdmin)
