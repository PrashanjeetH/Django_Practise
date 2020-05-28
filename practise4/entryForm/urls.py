from django.urls import path
from . import views
#define your urls here

urlpatterns = [
    path("", views.index, name = "index"),
    path("", views.page1, name = "page1"),
]
