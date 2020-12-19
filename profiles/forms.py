from django import forms
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.layout import Field
from django.forms import widgets
from cloudinary.forms import CloudinaryFileField

# TODO how to add google captcha?
class EmailInviteForm(forms.Form):
    name = forms.CharField(max_length=30,)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False, max_length=300, widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        """
        Use placeholders instead of labels and autofocus the first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Your name',
            'email': 'Your email',
            'to': 'Recipient email',
            'comment': 'Add a personal message?',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


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
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
