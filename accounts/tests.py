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
        
        
class SignupPageTests(TestCase):
   """Tests the existence of the sign up page (status code), that it 
   uses the correct template with the included and excluded html and 
   that it uses the correct form and urls."""
   
      
   def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

   def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'I shouldn\'t be on the page.')
        
   username = 'newuser'
   email = 'newuser@email.com'     

   def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                         [0].email, self.email) 