from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('apply/', views.apply, name='apply'),
]