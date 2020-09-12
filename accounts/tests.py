from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

class TestCustomUser(TestCase):
    """Test user creation."""
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'username',
            email= 'user@mail.com',
            password= 'userpass',
        )
        self.assertEqual(user.username, 'username')
        self.assertEqual(user.email, 'user@mail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = 'superusername',
            email= 'superuser@mail.com',
            password= 'superuserpass',
        )
        self.assertEqual(admin_user.username, 'superusername')
        self.assertEqual(admin_user.email, 'superuser@mail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)   
        