from django.test import TestCase
from .models import Post

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title='This is a new title')
        
    def test_post_title(self):
        post = Post.objects.get(title='This is a new title')
        self.assertEquals(post.title, 'This is a new title')
        
    def test_post_string_method_returns_title(self):
        post = Post.objects.get(title='This is a new title')
        self.assertEqual(str(post), 'This is a new title')
