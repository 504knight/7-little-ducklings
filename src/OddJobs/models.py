from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import connection
from enum import IntEnum, unique

@unique
class UserType(IntEnum):
    CUSTOMER = 0
    WORKER = 1
    OWNER = 2
    ADMIN = 3


class User(AbstractUser):

    userType = models.CharField(max_length=10, null=False)

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40, unique=True, null=False)
    #inherits first_name, last_name, email, is_active, and password fields already from parent model
    balance = models.FloatField(null=False, default=0)
    type = models.SmallIntegerField(null=False, default=UserType.CUSTOMER)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_jobs(self):
        type_condition = 'customer_id' if self.type == UserType.CUSTOMER else 'worker_id'
        return Job.objects.raw(f"SELECT * FROM OddJobs_jobs WHERE {type_condition} = %s", [self.id])

    def get_job_history(self, start_date, end_date):
        type_condition = 'customer_id' if self.type == UserType.CUSTOMER else 'worker_id'
        return Job.objects.raw(f"SELECT * FROM OddJobs_jobs WHERE {type_condition} = %s AND completed = %s AND start_time >= %s AND start_time <= %s",
                               [self.id, True, start_date, end_date])

    #initially start_time will be the start time of the time window in which the customer wants the job completed
    #when worker accepts a job update job start_time to be the time they have chosen to start the job

    #method needs testing to see how django stores datetime in sqlite (no datetime data-storage-type in sqlite, can be declared as datetime, but stored text or int)
    def get_future_jobs(self):
        type_condition = 'customer_id' if self.type == UserType.CUSTOMER else 'worker_id'
        return Job.objects.raw(f"SELECT * FROM OddJobs_jobs WHERE {type_condition} = %s AND start_time >= DATE('now')", [self.id])

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
    rating = models.FloatField(null=True)

    class Meta:
        db_table = 'jobs'


