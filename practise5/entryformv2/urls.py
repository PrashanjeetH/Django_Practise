from django.urls import path
from . import views
#Define your ruls here

urlpatterns = [
    path("", views.index, name = "index"),
    path("signup", views.signup, name = "signup"),
    path("loggedin", views.loggedin, name = "loggedin"),
    path("login", views.login, name = "login"),

]
