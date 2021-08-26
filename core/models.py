from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=60, null=True)
    mobile = models.CharField(max_length=13, null=True)
    state = models.TextField(max_length=30, null=True)
    country = models.CharField(max_length=40, null=True)
