from django import forms
from django.forms.widgets import MultiWidget,Media
from .models import Album, Asset


class CreateAlbumModelForm(forms.ModelForm):
      class Meta:
            model = Album
            fields = ('title', 'description', 'is_public')
            

class AssetModelForm(forms.ModelForm):
      class Meta:
            model = Asset
            fields = ('album', 'title', 'description', 'media', 'tags')
      