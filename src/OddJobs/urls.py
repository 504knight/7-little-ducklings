from django.urls import path

from . import views

app_name = 'OddJobs'
urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_test, name='login'),
    path('logout', views.logout_view, name="logout"),
    path('new_user', views.new_user, name="new_user"),
    path('create_user', views.create_user, name="create_user"),
    path('delete_user', views.delete_user, name='delete_user'),
    path('admin', views.admin, name="admin"),
    path('job_history', views.job_history_page, name="job_history"),
    path('job_history_listings', views.job_history_listings, name="job_history_listings"),
    path('<int:job_id>/rating_popup', views.rating_popup, name="rating_popup"),
    path('<int:job_id>/submit_rating', views.submit_rating, name="submit_rating"),
    path('accept_job', views.accept_job, name="accept_job"),
    path('<int:job_id>/complete_job', views.complete_job, name="complete_job"),
    path('<int:job_id>/remove_job', views.remove_job, name="remove_job"),
    path('<int:job_id>/cancel_job', views.cancel_job, name="cancel_job"),
    path('available_jobs', views.worker_available_jobs, name="available_jobs"),
    path('accepted_jobs', views.worker_accepted_jobs, name="accepted_jobs"),
    path('active_jobs', views.customer_active_jobs, name="active_jobs"),
    path('balance_page/', views.balance_page, name="balance_page"),
    path('balance_page/<str:err_msg>/', views.balance_page, name="balance_page"),
    path('update_balance', views.update_balance, name="update_balance"),
    path('request_username/<str:email_address>/', views.request_username, name="request_username"),
    path('reset_code/<str:email_address>/', views.reset_code, name="reset_code"),
    path('reset_password', views.reset_password, name="reset_password"),
    path('account_info', views.account_info, name="account_info"),
    path('account_reset/', views.account_reset, name="account_reset"),
    path('account_reset/<str:err_msg>/', views.account_reset, name="account_reset"),
    path('archive_user', views.archive_user, name="archive_user"),
    path('new_job', views.new_job, name="new_job"),
    path('create_job', views.create_job, name="create_job"),
]

