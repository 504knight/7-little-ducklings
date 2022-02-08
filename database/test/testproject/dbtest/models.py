from django.db import models

# Create your models here.
from django.db import models
from django.db import connection


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, unique=True, null=False)
    firstname = models.TextField(null=False)
    lastname = models.TextField(null=False)
    email = models.EmailField(null=False)
    balance = models.FloatField(null=False)
    archived = models.BooleanField(null=False)

    class Meta:
        db_table = 'users'


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='+')
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    job_title = models.CharField(max_length=200, null=False)
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
