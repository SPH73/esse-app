from django.db import models

class ProfileQuerySet(models.QuerySet):
    def get_users_friends(self, user):
        return self.filter(profile__user=user)
    
    def get_users_relations(self, user):
        return self.filter(profile__user=user)
        
class ProfileManager(models.Manager):
    def get_queryset(self):
        return ProfileQuerySet(self.model, using=self._db)
    
    def get_users_friends(self, profile):
        return self.get_queryset().get_users_friends(profile)
    
    def get_users_relations(self, profile):
        return self.get_queryset().get_users_relations(profile)


class FriendRequestQuerySet(models.QuerySet):
    def get_users_sent_requests(self, user):
        return self.filter(from_user__user=user)
    
    def get_user_sent_requests(self, user):
        return self.filter(from_user__user=user)
    
    def get_user_rec_requests(self, user):
        return self.filter(to_user__user=user)
        
class FriendReqestManager(models.Manager):
    
    def get_queryset(self):
        return FriendRequestQuerySet(self.model, using=self._db)    
