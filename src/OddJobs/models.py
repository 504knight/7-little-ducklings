from django.contrib.auth.models import AbstractUser
from django.db import models, connection
from enum import IntEnum, unique
from datetime import datetime
import re

@unique
class UserType(IntEnum):
    CUSTOMER = 0
    WORKER = 1
    OWNER = 2
    ADMIN = 3


class User(AbstractUser):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40, unique=True, null=False)
    #inherits first_name, last_name, email, is_active, and password fields already from parent model
    balance = models.FloatField(null=False, default=0)
    type = models.SmallIntegerField(null=False, default=UserType.CUSTOMER)
    email = models.EmailField(max_length=254, null=False, unique=True) #must override because default field in super does not enforce a unique constraint

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_jobs(self):
        type_condition = 'customer_id' if self.type == UserType.CUSTOMER else 'worker_id'
        return Job.objects.raw(f"SELECT * FROM jobs WHERE {type_condition} = %s", [self.id])

    def get_job_history(self, start_date, end_date):
        type_condition = 'customer_id' if self.type == UserType.CUSTOMER else 'worker_id'
        return Job.objects.raw(f"SELECT * FROM jobs WHERE {type_condition} = %s AND completed = %s AND start_time >= %s AND start_time <= %s",
                               [self.id, True, start_date, end_date])

    def get_avg_rating(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT AVG(rating) FROM jobs WHERE worker_id=%s", [self.id])
            row = cursor.fetchone()
            return row[0]


    #initially start_time will be the start time of the time window in which the customer wants the job started
    #when worker accepts a job update job start_time to be the time they have chosen to start the job

    def get_future_jobs(self):
        type_condition = 'customer_id' if self.type == UserType.CUSTOMER else 'worker_id'
        return Job.objects.raw(f"SELECT * FROM OddJobs_jobs WHERE {type_condition} = %s AND start_time >= DATE('now')", [self.id])

    def accept_job(self, job, chosen_start_time):
        """
        accept_job accepts a job for the worker

        :param job: type-Job object, the Job the worker wishes to accept
        :param chosen_start_time: type-Datetime object, the time the worker wishes to start the job (Must be within customer's given start window)
        """
        if self.type != UserType.WORKER:
            print("Only workers can accept jobs.")
            return False
        elif chosen_start_time < job.start_time or chosen_start_time > job.end_time:
            #don't allow a worker to choose a job at a time that is not within the customer's time window
            return False
        else:
            job.worker = self
            job.start_time = chosen_start_time
            job.save()
            return True

    def update_balance(self, action, amount):
        if re.fullmatch("^\\d+\\.{0,1}\\d{0,2}$", str(amount)) is not None and float(amount) >= 0:
            if int(action) == 0: #deposit
                self.balance += float(amount)
                self.save()
            elif int(action) == 1 and self.balance >= float(amount): #withdraw
                self.balance -= float(amount)
                self.save()
            else:
                return False
            return True
        return False


    @staticmethod
    def is_valid_time(chosen_time, start_time, end_time):
        dt_chosen = datetime.strptime(chosen_time, '%y-%m-%d %H:%M:%S')

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


