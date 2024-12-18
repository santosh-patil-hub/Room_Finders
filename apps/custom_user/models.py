from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True,blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True,blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default_profile.jpg',blank=True, null=True)
    bio = models.TextField(max_length=500,blank=True, null=True)
    location = models.CharField(max_length=100,blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    