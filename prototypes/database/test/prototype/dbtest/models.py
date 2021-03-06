from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import connection


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, unique=True, null=False)
    #inherits first_name, last_name, email, and is_active fields already from parent model
    balance = models.FloatField(null=False)

    class Meta:
        db_table = 'users'


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='+')
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    job_title = models.CharField(max_length=200, null=False)
    job_description = models.TextField(null=False)
    location = models.TextField(null=False)
    price = models.FloatField(null=False)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    completed = models.BooleanField(null=False)

    class Meta:
        db_table = 'jobs'


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.OneToOneField(Job, null=False, related_name='+', on_delete=models.CASCADE)
    score = models.SmallIntegerField(null=True)

    class Meta:
        db_table = "reviews"