from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.login_test, name='page'),
    path('logout', views.logout_view, name='logout'),
]