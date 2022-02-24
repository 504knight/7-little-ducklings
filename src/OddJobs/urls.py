from django.urls import path

from . import views

app_name = 'OddJobs'
urlpatterns = [
    path('', views.index, name="index"),
]