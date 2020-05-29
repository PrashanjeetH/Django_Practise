from django.urls import path
from . import views
#Define your ruls here

urlpatterns = [
    path("", views.index, name = "index"),
    path("signup", views.signup, name = "signup")
]
