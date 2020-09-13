from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    # Forms to add and change user instances.
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # Fields to display the CustomUser model
    list_display = ['email', 'username', 'last_login', 'date_joined',]

admin.site.register(CustomUser, CustomUserAdmin)