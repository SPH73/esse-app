from django import forms
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.layout import Field
from django.forms import widgets
from cloudinary.forms import CloudinaryFileField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

User = get_user_model()


class UserEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)


class EmailInviteForm(forms.Form):
    name = forms.CharField(max_length=30,)
    to = forms.EmailField()
    comment = forms.CharField(
        required=False, max_length=300, widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        """
        Use placeholders instead of labels and autofocus the first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Your name',
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


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('status', 'avatar')

    status = forms.CharField(
        label='',
      )

    avatar = CloudinaryFileField(
    options={
        'folder': 'Esse/user_uploads/avatars',
        'use_filename': True,
        'overwrite': True,
        'resource_type': 'auto',
        'transformation': [
            {'width': 200, 'height': 200, 'gravity': "face", 'crop': "thumb"}
        ]
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
