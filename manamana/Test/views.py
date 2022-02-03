from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect

# Create your views here.

@login_required
def index(request):
        return HttpResponse("Logged in as: " + request.user.username)

@login_required
def login_test(request):
    return HttpResponse("It Worked")


def logout_view(request):
    logout(request)
    return redirect('/test')
