from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User


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
    return render(request, "OddJobs/login_test.html")

def new_user(request):
    return render(request, 'OddJobs/input_new_user.html')

def create_user(request):
    username = request.POST['username']
    email = request.POST['email']
    fname = request.POST['fname']
    lname = request.POST['lname']
    balance = 0
    password = request.POST['password']

    user_to_be_made = User(username=username, balance=balance)

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


def admin(request):
    if request.user.userType != "admin":
        return redirect('OddJobs:index')
    else:
        users = User.objects.all()
        context = {
            'users': users
        }
        return render(request, 'OddJobs/admin.html', context)