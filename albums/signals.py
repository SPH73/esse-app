import cloudinary
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Asset
        
@receiver(pre_delete, sender=Asset)
def pre_delete_asset(self, sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.asset.public_id)
    print('Asset deleted from Cloudinary')
        
