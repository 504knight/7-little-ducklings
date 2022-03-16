from django.urls import path

from . import views

app_name = 'OddJobs'
urlpatterns = [
    path('', views.index, name="index"),
    path('logout', views.logout_view, name="logout"),
    path('new_user', views.new_user, name="new_user"),
    path('create_user', views.create_user, name="create_user"),
    path('delete_user', views.delete_user, name='delete_user'),
    path('admin', views.admin, name="admin"),
    path('job_history', views.job_history_page, name="job_history"),
    path('job_history_listings', views.job_history_listings, name="job_history_listings"),
    path('available_jobs', views.worker_available_jobs, name="available_jobs"),
    path('accepted_jobs', views.worker_accepted_jobs, name="accepted_jobs"),
    path('active_jobs', views.customer_active_jobs, name="active_jobs"),
]