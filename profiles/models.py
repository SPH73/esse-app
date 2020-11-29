from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

def user_dir(instance, filename):
    return f'avatars/user_{instance.user.username}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatar.png',upload_to=user_dir)
    status = models.TextField(max_length=350, default='No status ...')
    relations = models.ManyToManyField(User, related_name='relations', blank=True)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.user.username)