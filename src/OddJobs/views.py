from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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
            print(str(request.user))
            job_history = JobHistory.get_job_history(request)
            return render(request, 'OddJobs/job_history_listings.html', {'user': request.user, 'job_history': job_history, 'range': range(1, 6)})
        except:
            raise Http404("Error obtaining job history")


def rating_popup(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if not request.user.is_authenticated or job.customer != request.user:
        return redirect('OddJobs:index')
    return render(request, 'OddJobs/rating_popup.html', {'job_id': job_id})


def submit_rating(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if not request.user.is_authenticated or job.customer != request.user:
        return redirect('OddJobs:index')
    try:
        selected_rating = int(request.POST['rating'])
    except:
        raise Http404("Error Submitting Rating")
    else:
        job.rating = selected_rating
        job.save()
        return redirect('OddJobs:job_history')


def balance_page(request, err_msg=""):
    print("Balance Pager error message: " + str(err_msg))
    if request.user.is_authenticated:
        return render(request, 'OddJobs/balance_page.html', {'err_msg': err_msg})
    else:
        return redirect('OddJobs:index')


def update_balance(request):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    try:
        if not request.user.update_balance(request.POST['action'], request.POST['amount']):
            return redirect('OddJobs:balance_page', err_msg="Invalid amount.")
    except:
        return redirect('OddJobs:balance_page', err_msg="Error updating balance.")
    else:
        return redirect('OddJobs:balance_page')




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
        start_date = request.GET['start_date']
        end_date = request.GET['end_date']

        print(f'Current User: {current_user}\nStart Date: {start_date}\nEnd Date: {end_date}')

        return list(current_user.get_job_history(start_date, end_date))

