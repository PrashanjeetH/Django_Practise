from django.urls import path
from . import views
#Define your urls here

urlpatterns = [
    path("", views.home_view, name = "index")
]
