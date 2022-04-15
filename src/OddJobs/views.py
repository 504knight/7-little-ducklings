from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Job
from django.http import Http404
from django.conf import settings
from datetime import date, datetime
from django.core import serializers
import json
import re
from django.urls import reverse

from .forms import NewUserForm

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

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            return redirect('OddJobs:create_user')

    else:
        form = NewUserForm()

    return render(request, 'OddJobs/input_new_user.html', {'form': form})


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


def job_history_listings(request):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    elif 'start_date' not in request.GET or 'end_date' not in request.GET:
        raise Http404("Missing required parameters - must have start_date and end_date")
    else:
        try:
            print(str(request.user))
            job_history = JobHistory.get_job_history(request)
            for job in job_history[:]:
                if not job.rating:
                    job_history.remove(job)
            return render(request, 'OddJobs/job_history_listings.html', {'user': request.user, 'job_history': job_history, 'range': range(1, 6)})
        except:
            raise Http404("Error obtaining job history")

@login_required()
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
        return response

@login_required()
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

@login_required()
def account_info(request):
    if request.user.is_authenticated:
        return render(request, 'OddJobs/account_info.html')
    else:
        return redirect('OddJobs:login')


def account_reset(request, err_msg=""):
    return render(request, 'OddJobs/account_reset.html', {'err_msg': err_msg})


def request_username(request, email_address):
    try:
        if Validation.is_valid_email(email_address):
            user = User.objects.get(email=email_address)
        else:
            return HttpResponse("Please enter a valid email address.")
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
        if Validation.is_valid_email(email_address):
            user = User.objects.get(email=email_address)
        else:
            return HttpResponse("Please enter a valid email address.")
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
        if Validation.is_valid_email(email_address):
            code = int(request.POST['code'])
            newPassword = request.POST['password']
            user = User.objects.get(email=email_address)
        else:
            return redirect('OddJobs:account_reset', err_msg="Please enter a valid email.")

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

def accept_job(request):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    try:
        selected_date = request.POST['date']
    except:
        raise Http404("Error: Need Start Date")
    else:
        job_id = request.POST['job_id']
        job = Job.objects.get(id=job_id)
        if (job.worker == None):
            if (request.user.accept_job(job_id, selected_date)):
                return redirect('OddJobs:accepted_jobs')
            else:
                job_data = serializers.serialize("json", request.user.get_all_jobs())
                return render(request, 'OddJobs/workeravailable.html', {'jobs': json.dumps(job_data), 'error_message': "Select a date in the preferred window!"})
        else:
            job_data = serializers.serialize("json", request.user.get_all_jobs())
            return render(request, 'OddJobs/workeravailable.html', {'jobs': json.dumps(job_data), 'error_message': "Job already accepted!"})
            
        

def remove_job(request, job_id):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    else:
        job = Job.objects.get(id=job_id)
        if (job.customer != request.user):
            return redirect('OddJobs:index')
        else:
            job.delete()
            return redirect('OddJobs:active_jobs')

def cancel_job(request, job_id):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    else:
        job = Job.objects.get(id=job_id)
        if (job.worker != request.user):
            return redirect('OddJobs:index')
        else:
            job.worker = None
            job.save()
            return redirect('OddJobs:accepted_jobs')

def complete_job(request, job_id):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    job = Job.objects.get(id=job_id)
    job.completed = True
    job.save()
    return redirect('OddJobs:accepted_jobs')

def confirm_and_rate(request, job_id):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    job = Job.objects.get(id=job_id)
    price = job.price
    owner_cut = price * 0.05
    if (job.customer.update_balance(1, price)):
        job.worker.update_balance(0, price - owner_cut)
        owner = User.objects.get(type=3)
        owner.update_balance(0, owner_cut)
        return render(request, 'OddJobs/rating_popup.html', {'job_id': job_id, 'start_date': job.start_time, 'end_date': job.end_time})
    else:
        job_data = serializers.serialize("json", request.user.get_jobs())
        return render(request, 'OddJobs/customeractive.html', {'jobs': json.dumps(job_data), 'error_message': "Not enough funds in your account!"})
    

@login_required()
def new_job(request):
    if not request.user.is_authenticated:
        return redirect('OddJobs:index')
    elif 'error_message' in request.GET:
        print(request.GET['error_message'])
        return render(request, 'OddJobs/input_new_job.html', {'error_message': request.GET['error_message']})
    elif 'success' in request.GET:
        return render(request, 'OddJobs/job_created.html')
    return render(request, 'OddJobs/input_new_job.html')


def create_job(request):
    try:
        error_message = Validation.validate_job_info(request)
        if error_message == "":
            title = request.POST['title']
            description = request.POST['description']
            location = request.POST['location']
            price = request.POST['price']
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
            duration = request.POST['duration']
            job_obj = Job(customer=request.user, job_title=title, job_description=description, location=location, price=price, start_time=start_date, end_time=end_date, duration=duration, completed=False)
            job_obj.save()
        else:
            response = redirect('OddJobs:new_job')
            response['Location'] += f"?error_message={error_message}"
            return response
    except Exception as e:
        print(f"Exception: {e}")
        response = redirect('OddJobs:new_job')
        response['Location'] += "?error_message=You must fill all fields.  If error persists, contact customer service department."
        return response
    else:
        response = redirect('OddJobs:new_job')
        response['Location'] += "?success=true"
        return response


class JobHistory:

    @staticmethod
    def get_job_history(request):
        current_user = request.user
        start_date = request.GET['start_date']
        end_date = request.GET['end_date']

        print(f'Current User: {current_user}\nStart Date: {start_date}\nEnd Date: {end_date}')
        if Validation.is_valid_date(start_date) and Validation.is_valid_date(end_date):
            return list(current_user.get_job_history(start_date, end_date))
        empty_list = []
        return empty_list


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

class Validation:

    date_regex = '^\d{4}-\d{2}-\d{2}$'
    date_time_regex = '^\d{4}-\d{2}-\d{2}[a-zA-Z:0-9]+$'
    email_regex = '^\w+@\w+\.\w+$'
    money_regex = "^\d+\.{0,1}\d{0,2}$"

    @staticmethod
    def validate_job_info(request):
        try:
            parameters = request.POST
            title = parameters['title']
            description = parameters['description']
            location = parameters['location']
            price = str(parameters['price'])
            start_date = parameters['start_date']
            print(start_date)
            end_date = parameters['end_date']
            print(end_date)
            duration = parameters['duration']
            print(duration)
            duration = str(duration)
        except:
            print("Caught Exception")
            return "Unable to process your request."
        else:
            valid_start_date = Validation.is_valid_datetime(start_date) and Validation.is_future_date(start_date)
            date_comparison = Validation.compare_dates(end_date, start_date)
            valid_end_date = Validation.is_valid_datetime(end_date) and (date_comparison == 1 or date_comparison == 0)
            print(f"Valid Start Date: {valid_start_date}")
            print(f"Valid End Date: {valid_end_date}")
            if not re.match('^[a-zA-Z\s]+$', title):
                return "Title must only contain letters and spaces."
            elif not re.match('^[\d\w\.\s]+$', description):
                return "The description can only contain letters, numbers, periods, and spaces."
            elif not re.match('^[\d\w,\.\s]+$', location):
                return "The location can only contain letters, numbers, periods, commas, and spaces."
            elif not Validation.is_valid_money(price):
                return "The price you have entered is invalid. It must contain a at least one digit."
            elif not valid_start_date or not valid_end_date:
                return "One or more of the dates you have entered is invalid or is in the past."
            elif not re.match('^[1-9][0-9]*$', duration):
                return "You have entered an invalid duration. Must be a whole number"
            else:
                return ""

    @staticmethod
    def is_valid_date(value):
        value = str(value)
        return re.match(Validation.date_regex, value)

    @staticmethod
    def is_valid_datetime(value):
        return re.match(Validation.date_time_regex, value)

    #only for use with datetimes! not with just dates
    @staticmethod
    def is_future_date(value):
        date = Validation.cvt_to_datetime(value)
        return date >= datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

    @staticmethod
    def compare_dates(date1, date2):
        date1 = Validation.cvt_to_datetime(date1)
        date2 = Validation.cvt_to_datetime(date2)
        if date1 > date2 :
            return 1;
        elif date2 > date1 :
            return -1
        return 0

    @staticmethod
    def cvt_to_datetime(dateStr):
        dateStr = str(dateStr)
        arr = dateStr.split('-')
        year = int(arr[0])
        month = int(arr[1])
        day = int(arr[2][:2])
        date = datetime(year, month, day)
        return date


    @staticmethod
    def is_valid_email(str):
        return re.match(Validation.email_regex, str)

    @staticmethod
    def is_valid_money(str):
        return re.match(Validation.money_regex, str)




