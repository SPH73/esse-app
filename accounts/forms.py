from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    """A custom form for creating new users that extends UserCreationForm."""
    
    class Meta:
        """specify CustomUser model"""
        model = get_user_model()
        fields = ('email', 'username',)
        

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)