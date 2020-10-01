from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.



class Membership(models.Model):
    MEMBERSHIP_CHOICES =[
        ('Free', 'Free'),
        ('Basic', 'Basic'),
        ('Pro', 'Pro')
    ]
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, default='Free', max_length=30)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
    
    def __str__(self):
       return self.membership_type

class UserMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_membership')
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, related_name='user_membership', null=True)
    
    def __str__(self):
       return self.user.username
   

class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, related_name='subscription', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    
    def __str__(self):
      return self.user_membership.user.username   