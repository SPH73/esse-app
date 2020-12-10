from django import forms
from .models import Album, Asset


class CreateAlbumModelForm(forms.ModelForm):
      class Meta:
            model = Album
            fields = ('title', 'description', 'is_public')
            

class AssetModelForm(forms.ModelForm):
      class Meta:
            model = Asset
            fields = ('title', 'description', 'media', 'tags')
      