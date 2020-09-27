from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework.serializers import HyperlinkedModelSerializer

User = get_user_model()

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        

class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']