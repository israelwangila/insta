from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='default.jpeg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.user, self.bio)


    def save_profile(self):
        self.save()