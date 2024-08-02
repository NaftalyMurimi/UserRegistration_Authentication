
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   
   path("home/", views.home, name="home"),
   path("signin/", views.signin, name="signin"),
   path("register/", views.register, name="register"),
   path("dashboard/", views.dashboard, name="dashboard"),
   path("logout/", views.logout, name="logout"),
]
