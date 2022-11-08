from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
app_name = "GirinkaApp"
urlpatterns = [
	path('', views.home, name="home"),
    path('login1/', views.login1, name="login1"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login")
	
]