import cloudinary
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Asset
        
# @receiver(pre_delete, sender=Asset)
# def pre_delete_asset(self, sender, instance, **kwargs):
#     print("Delete album signal")
#     result = cloudinary.uploader.destroy(instance.asset.public_id)
#     print(result)
        
