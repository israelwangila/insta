from django.test import TestCase
from .models import Post

# Create your tests here.

class PostTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.alex=Post(caption="We are who we are.")

    #Testing instance

    def test_instance(self):
        self.assertTrue(isinstance(self.alex,Post))

    #Testing Save method
    def test_save_method(self):
        self.alex.save_post()
        post= post.objects.all()
        self.assertTrue(len(post) > 0)