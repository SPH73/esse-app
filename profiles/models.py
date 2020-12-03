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
    
    
    def get_friends(self):
        return self.friends.all()
    
    def get_friends_count(self):
        return self.friends.all().count()
    
    def get_relations(self):
        return self.relations.all()
    
    def get_relations_count(self):
        return self.relations.all().count()
    
    def __str__(self):
        return str(self.user.username)