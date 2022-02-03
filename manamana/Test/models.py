from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserObject(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=40)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

