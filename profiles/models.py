from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    avatar = CloudinaryField('avatar', default='Esse/avatar.png')
    status = models.TextField(max_length=350, default='No status ...')
    relations = models.ManyToManyField(User, related_name='relations', blank=True)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def get_url_path(self):
        return '/profiles/%s/' % self.slug
        
    def get_friends(self):
        return self.friends.all()
    
    def get_friends_count(self):
        return self.friends.all().count()
    
    def add_friend(self, user):
        """
        Add user to friends
        """
        if user not in self.friends.all():
            self.friends.add(user)
            
    def delete_friend(self, user):
        """
        Remove user from friends
        """
        if user in self.friends.all():
            self.friends.remove(user)
    
    def get_relations(self):
        return self.relations.all()
    
    def get_relations_count(self):
        return self.relations.all().count()
    
    def add_relation(self, user):
        """
        Add friend to relations
        """
        if user in self.friends.all():
            if user not in self.relations.all():
                self.relations.add(user)
    
    def remove_relation(self, user):
        """
        Revert relation back to friends
        """
        if user in self.relations.all():
            self.relations.remove(user)
            self.friends.add(user)
       
    def __str__(self):
        return str(self.user.username)
    
    def save(self, *args, **kwargs):
        add_slug = str(self.user)
        self.slug = add_slug
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('profiles:user_detail', args=[self.slug])
  

STATUS_CHOICES = (
        ('Requested', 'Requested'),
        ('Confirmed', 'Confirmed')
)


class FriendRequest(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES)
    is_family = models.BooleanField(default=False)
    
    def get_friend_requests_count(self):
        return self.to_user.all().count()
    
    def __str__(self):
        return f"From {self.from_user}, to {self.to_user} on {self.created.strftime('%d-%m-%Y')}"
