from django import forms
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.layout import Field
from django.forms import widgets
from cloudinary.forms import CloudinaryFileField


def avatar_media_dir():
    folder = 'Esse/user_uploads/avatars'
    return folder

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('status', 'avatar')
    
    status = forms.CharField(
        label = '',
      )
    
    avatar = CloudinaryFileField(
    options = {
        'folder': 'Esse/user_uploads/avatars',
        'use_filename': True,
        'overwrite': True,
        'resource_type': 'auto',
        'auto_tagging': 0.8,
    }
      )
        
    def __init__(self, *args, **kwargs):
        """
        Remove the labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'status': 'Status',
            'avatar': 'Avatar'
        }

        self.fields['status'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders
            self.fields[field].label = False
