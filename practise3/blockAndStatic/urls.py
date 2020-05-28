from django.urls import path
from . import views

#create your URLs here

urlpatterns = [
    path("",views.index, name = "index"),
    path("<int:name_id>",views.page1, name = "page1"),
]
