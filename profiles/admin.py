from django.contrib import admin
from .models import Profile, FriendRequest

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'avatar',
        'created',
        'updated',
    )
    ordering = ('-updated',)

class FriendRequestAdmin(admin.ModelAdmin):
    list_display = (
        'from_user',
        'to_user',
        'status',
        'created',
        'is_family'
    )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(FriendRequest, FriendRequestAdmin)
