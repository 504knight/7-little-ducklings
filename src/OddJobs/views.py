from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User
from django.http import Http404


# Create your views here.

def index(request):
    context = {
        'users': User.objects.all(),
        'request': request,
               }

    return render(request, 'OddJobs/index.html', context)

@login_required
def login_test(request):
    return render(request, "OddJobs/login_test.html")

def new_user(request):
    return render(request, 'OddJobs/input_new_user.html')

def create_user(request):
    username = request.POST['username']
    email = request.POST['email']
    fname = request.POST['fname']
    lname = request.POST['lname']
    password = request.POST['password']

    user_to_be_made = User(username=username)

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

    return redirect('OddJobbs:index')

#job-history
def job_history_page(request):
    print("unimplemented")

def job_history_data(request):
    current_user = request.user
    context = {}
    if 'start_date' not in request.GET or 'end_date' not in request.GET:
        raise Http404("Missing required parameters - must have start_date and end_date")
    else:
        try:
            job_history = JobHistory.get_job_history(request)
        except:
            raise Http404("Error obtaining job history")



class JobHistory:

    @staticmethod
    def get_job_history(request):
        current_user = request.user
        start_date = request.Get['start_date']
        end_date = request.Get['end_date']
        return list(current_user.get_job_history(start_date, end_date))



