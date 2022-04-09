from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Job
from django.http import Http404
from django.conf import settings
from datetime import date
from django.core import serializers
import json

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
    type = request.POST['type']
    balance = 0
    password = request.POST['password']

    user_to_be_made = User(username=username, password=password, first_name=fname, last_name=lname, email=email, type=type)

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
    if request.user.type != 3:
        return redirect('OddJobs:index')
    else:
        users = User.objects.all()
        jobs = Job.objects.all()
        context = {
            'users': users,
            'jobs': jobs
        }
        return render(request, 'OddJobs/admin.html', context)


@login_required()
def job_history_page(request):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    elif 'start_date' in request.GET and 'end_date' in request.GET: #if given default start and end date
        context = {'start_date': request.GET['start_date'], 'end_date': request.GET['end_date']}
    else:
        context = {}
    return render(request, 'OddJobs/job_history.html', context)


@login_required()
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
    try:
        start_date = request.GET['start_date']
        end_date = request.GET['end_date']
    except:
        raise Http404("Error getting rating page.")
    return render(request, 'OddJobs/rating_popup.html', {'job_id': job_id, 'start_date': start_date, 'end_date': end_date})


def submit_rating(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if not request.user.is_authenticated or job.customer != request.user:
        return redirect('OddJobs:index')
    try:
        selected_rating = int(request.POST['rating'])
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
    except:
        raise Http404("Error Submitting Rating")
    else:
        job.rating = selected_rating
        job.save()
        response = redirect('OddJobs:job_history')
        response['Location'] += f"?start_date={start_date}&end_date={end_date}"
        print(response['Location'])
        return response


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


def account_info(request):
    if request.user.is_authenticated:
        return render(request, 'OddJobs/account_info.html')
    else:
        return redirect('OddJobs:login')


def account_reset(request, err_msg=""):
    return render(request, 'OddJobs/account_reset.html', {'err_msg': err_msg})


def request_username(request, email_address):
    try:
        user = User.objects.get(email=email_address)
    except User.DoesNotExist:
        return HttpResponse("We were unable to find a user with that email address.")
    except:
        return HttpResponse("An error occurred.")
    else:
        user.email_user(subject='Your OddJobs Username', message=f"Your username is {user.username}",
                  from_email=settings.EMAIL_HOST_USER)
        return HttpResponse("success")


def reset_code(request, email_address):
    try:
        user = User.objects.get(email=email_address)
    except User.DoesNotExist:
        return HttpResponse("We were unable to find a user with that email address.")
    except:
        return HttpResponse("An error occurred.")
    else:
        msg = f"Your reset code is: {AccountInfo.get_six_digit_hash(user.email)}\n" \
              f"This code is valid until {date.today().strftime('%m/%d/%Y')} at 11:59 pm (MST)."
        user.email_user(subject='Password Reset Code', message=msg,
                  from_email=settings.EMAIL_HOST_USER)
        return HttpResponse("success")


def reset_password(request):
    try:
        email_address = request.POST['email']
        code = int(request.POST['code'])
        newPassword = request.POST['password']
        user = User.objects.get(email=email_address)
    except User.DoesNotExist:
        return redirect('OddJobs:account_reset', err_msg="We were unable to find a user with that email address.")
    except:
        return redirect('OddJobs:account_reset', err_msg="Please make sure you have entered your email, code, and new password.")
    else:
        if code == AccountInfo.get_six_digit_hash(user.email):
            user.set_password(newPassword)
            user.save()
            return redirect('OddJobs:login')
        else:
            return redirect('OddJobs:account_reset', err_msg="Incorrect code entered.")


def archive_user(request):
    if request.user.is_authenticated:
        user = request.user
        user.is_active = False
        user.save()
    return redirect('OddJobs:index')


def worker_available_jobs(request):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    job_data = serializers.serialize("json", request.user.get_all_jobs())
    return render(request, 'OddJobs/workeravailable.html', {'jobs': json.dumps(job_data)})


def worker_accepted_jobs(request):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    job_data = serializers.serialize("json", request.user.get_jobs())
    return render(request, 'OddJobs/workeraccepted.html', {'jobs': json.dumps(job_data), 'user_id': request.user.id})


def customer_active_jobs(request):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    job_data = serializers.serialize("json", request.user.get_jobs())
    return render(request, 'OddJobs/customeractive.html', {'jobs': json.dumps(job_data)})

def accept_job(request, job_id):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    try:
        selected_date = request.POST['date']
    except:
        raise Http404("Error: Need Start Date")
    else:
        if (request.user.accept_job(job_id, selected_date)):
            return redirect('OddJobs:accepted_jobs')
        else:
            return redirect('OddJobs:available_jobs')

def complete_job(request, job_id):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    job = Job.objects.get(id=job_id)
    job.completed = True
    job.save()
    price = job.price
    if (job.customer.update_balance(1, price)):
        job.worker.update_balance(0, price)
    else:
        print("Not enough money in customer balance.")
    return redirect('OddJobs:accepted_jobs')


def new_job(request):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    return render(request, 'OddJobs/input_new_job.html')


def create_job(request):
    title = request.POST['title']
    description = request.POST['description']
    location = request.POST['location']
    price = request.POST['price']
    start_date = request.POST['start_date']
    end_date = request.POST['end_date']
    duration = request.POST['duration']

    job_obj = Job(customer=request.user, job_title=title, job_description=description, location=location, price=price, start_time=start_date, end_time=end_date, duration=duration, completed=False)
    job_obj.save()

    return render(request, 'OddJobs/job_created.html')


class JobHistory:

    @staticmethod
    def get_job_history(request):
        current_user = request.user
        start_date = request.GET['start_date']
        end_date = request.GET['end_date']

        print(f'Current User: {current_user}\nStart Date: {start_date}\nEnd Date: {end_date}')

        return list(current_user.get_job_history(start_date, end_date))


class AccountInfo:

    # not a great way to do identity verification, but didn't want to change the models again
    @staticmethod
    def get_six_digit_hash(string):
        string = str(date.day) + string[0:2] + str(date.month) + string[2:]
        stop = int(len(string) * 0.75)
        bytes = string[0:stop].encode()  # default encoding is utf-8
        hash = 0
        for byte in bytes:
            hash += byte
            hash += (hash << 10)
            hash ^= (hash >> 6)
        hash += (hash << 3)
        hash ^= (hash >> 11)
        hash += (hash << 15)

        return hash % 1000000
