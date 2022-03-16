from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User, Job
from django.http import Http404


# Create your views here.

def admin_check(user):
    return user.username == "Matthew"

def index(request):
    context = {
        'users': User.objects.all(),
        'request': request,
               }

    return render(request, 'OddJobs/index.html', context)


@login_required
def login_test(request):
    context = {
        'users': User.objects.all(),
        'request': request,
    }
    return render(request, "OddJobs/index.html", context)

def new_user(request):
    return render(request, 'OddJobs/input_new_user.html')

def create_user(request):
    username = request.POST['username']
    email = request.POST['email']
    fname = request.POST['fname']
    lname = request.POST['lname']
    balance = 0
    password = request.POST['password']

    user_to_be_made = User(username=username, password=password, first_name=fname, last_name=lname, email=email)

    user_to_be_made.set_password(password)

    user_to_be_made.save()

    context = {
        'username': user_to_be_made.username,
        'password': user_to_be_made.password,
    }

    login(request, user=user_to_be_made)

    return render(request, 'OddJobs/user_created.html', context=context)


def logout_view(request):
    logout(request)

    return redirect('OddJobs:index')


def delete_user(request):

    if request.user.is_authenticated:
        request.user.delete()
    return redirect('OddJobs:index')

@login_required()
def admin(request):
    if request.user.userType != "admin":
        return redirect('OddJobs:index')
    else:
        users = User.objects.all()
        jobs = Job.objects.all()
        context = {
            'users': users,
            'jobs': jobs
        }
        return render(request, 'OddJobs/admin.html', context)
    return redirect('OddJobbs:index')

#job-history
def job_history_page(request):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    return render(request, 'OddJobs/job_history.html', {})


def job_history_listings(request):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    elif 'start_date' not in request.GET or 'end_date' not in request.GET:
        raise Http404("Missing required parameters - must have start_date and end_date")
    else:
        try:
            job_history = JobHistory.get_job_history(request)
            return render(request, 'OddJobs/job_history_listings.html', {'user': request.user, 'job_history': job_history})
        except:
            raise Http404("Error obtaining job history")

def worker_available_jobs(request):
    #if not request.user.is_authenticated:
        #return redirect('OddJobs:index')
    return render(request, 'OddJobs/workeravailable.html')

def worker_accepted_jobs(request):
    #if not request.user.is_authenticated:
        #return redirect('OddJobs:index')
    return render(request, 'OddJobs/workeraccepted.html')

def customer_active_jobs(request):
    #if not request.user.is_authenticated:
        #return redirect('OddJobs:index')
    return render(request, 'OddJobs/customeractive.html')

class JobHistory:

    @staticmethod
    def get_job_history(request):
        current_user = request.user
        start_date = request.Get['start_date']
        end_date = request.Get['end_date']
        return list(current_user.get_job_history(start_date, end_date))

