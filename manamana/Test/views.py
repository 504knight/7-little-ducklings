from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.template import loader
from .models import UserObject

# Create your views here.
from django.template import Template


def index(request):
    context = {
        'users': UserObject.objects.all(),
        'request': request,
               }

    return render(request, 'Test/home.html', context)

@login_required
def login_test(request):
    return render(request, "Test/login_test.html")

def new_user(request):
    return render(request, 'Test/input_new_user.html')

def create_user(request):

    username = request.POST['username']
    email = request.POST['email']
    fname = request.POST['fname']
    lname = request.POST['lname']
    password = request.POST['password']

    user_to_be_made = UserObject(username=username)

    user_to_be_made.set_password(password)

    user_to_be_made.save()

    context = {
        'username': user_to_be_made.username,
        'password': user_to_be_made.password,
    }

    login(request, user=user_to_be_made)

    return render(request, 'Test/user_created.html', context=context)


def logout_view(request):
    logout(request)

    return redirect('Test:home')


def delete_user(request):

    if request.user.is_authenticated:
        request.user.delete()

    return redirect('Test:home')
