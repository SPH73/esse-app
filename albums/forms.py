from django import forms
from .models import Album, Asset
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.layout import Field
from django.forms import widgets
from cloudinary.forms import CloudinaryFileField


class CreateAlbumModelForm(forms.ModelForm):
      class Meta:
            model = Album
            fields = ('title', 'is_public')

      is_public = forms.TypedChoiceField(
            label = 'Who do you want to share this album with?',
            choices = ((1, "Everyone"), (0, "Family")),
            coerce = lambda x: bool(int(x)),
            widget = forms.RadioSelect,
            initial = '1',
            required = True,
      )

      title = forms.CharField(
            label = 'Title',
            max_length = 80,
            required = True,
      )

      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_id = 'id-createAlbumModelForm'
            self.helper.layout = Layout(
                  Fieldset(
                  'Create your album',
                  'is_public',
                  'title',
                  ),
            )

def album_media_dir():
      folder_name = 'Esse/user_uploads/albums/user_{instance.profile}/{instance.album.slug}/{filename}'
      return folder_name


class AssetModelForm(forms.ModelForm):
      class Meta:
            model = Asset
            fields = ('title', 'media', 'tags')

      title = forms.CharField(
            label = 'Title',
            max_length = 80,
            required = True,
      )

      media = CloudinaryFileField(
            options = {
            'folder': album_media_dir(),
            'use_filename': True,
            'resource_type': 'auto',
            'auto_tagging': 0.8
            }
      )

      tags = forms.CharField(
            label = 'Tags',
            required = False,
            help_text = 'Comma, separated, list'
      )


      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_id = 'id-assetModelForm'
            self.helper.use_custom_control = True
            self.helper.layout = Layout(
                  Fieldset(
                  'Add your media',
                  'media',
                  'title',
                  'tags',
                  )
            )