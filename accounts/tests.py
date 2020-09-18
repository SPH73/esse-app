from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView

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
   that it uses the custom form and resolves the url path."""
   
   def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

   def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'I shouldn\'t be on the page.')

   def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

   def test_signup_view(self): 
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )