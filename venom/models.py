from unittest.util import _MAX_LENGTH
from django.db import models
from  django.contrib.auth.models import User
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=35)
    phone = models.CharField(max_length=12)
    desc =  models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
        
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name= 'Profile')
    image = models.ImageField(upload_to = 'pics', default= 'messi.jpeg')

    def __str__(self):
        return f'{self.user} Profile'
