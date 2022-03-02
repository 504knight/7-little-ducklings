from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import connection


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, unique=True, null=False)
    #inherits first_name, last_name, email, and is_active fields already from parent model
    balance = models.FloatField(null=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_jobs(self):
        return Job.objects.raw(f"SELECT * FROM OddJobs_jobs WHERE worker_id={self.id} OR customer_id={self.id}")

    #initially start_time will be the start time of the time window in which the customer wants the job completed
    #when worker accepts a job update job start_time to be the time they have chosen to start the job

    #method needs testing to see how django stores datetime in sqlite (no datetime data-storage-type in sqlite, can be declared as datetime, but stored text or int)
    def get_future_jobs(self):
        return Job.objects.raw(f"SELECT * FROM OddJobs_jobs WHERE (worker_id={self.id} OR customer_id={self.id}) AND start_time >= DATE('now')")

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
    duration = models.FloatField(null=False)
    completed = models.BooleanField(null=False)

    class Meta:
        db_table = 'jobs'


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.OneToOneField(Job, null=False, related_name='+', on_delete=models.CASCADE)
    score = models.SmallIntegerField(null=True)

    class Meta:
        db_table = "reviews"
