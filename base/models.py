from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Photos(models.Model):
    avatar =models.ImageField(null=True,default="default.webp")

class User(AbstractUser):
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(unique=True,null=True)
    bio=models.TextField(null=True)

    USERNAME_FIELD: 'email'
    REQUIRED_FIELDS = []

class Room(models.Model):
    name=models.CharField(max_length=333)
    description=models.TextField(null=True,blank=True)

    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name