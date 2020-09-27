import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse



User = get_user_model()

class Portfolio(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
