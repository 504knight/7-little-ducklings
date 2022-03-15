from django.urls import path

from . import views

app_name = 'OddJobs'
urlpatterns = [
    path('', views.index, name="index"),
    path('test', views.login_test, name='login_test'),
    path('logout', views.logout_view, name="logout"),
    path('new_user', views.new_user, name="new_user"),
    path('create_user', views.create_user, name="create_user"),
    path('delete_user', views.delete_user, name='delete_user'),
    path('job_history', views.job_history_page, name="job_history"),
    path('job_history_listings', views.job_history_listings, name="job_history_listings"),
]