from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

User = get_user_model()

def user_dir(instance, filename):
    return f'avatars/user_{instance.user.username}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
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
    
    def save(self, *args, **kwargs):
        add_slug = str(self.user)
        self.slug = add_slug
        super().save(*args, **kwargs)
    
STATUS_CHOICES = (
        ('Requested', 'Requested'),
        ('Confirmed', 'Confirmed')
)

class FriendRequest(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    is_relation = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES)