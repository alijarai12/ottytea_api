from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class User(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    password = models.CharField(max_length=80, unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"User {self.email}"
