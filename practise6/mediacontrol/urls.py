from django.urls import path
from . import views

# Define your url link here

urlpatterns = [
    path("", views.home, name = "home"),
    path("upload", views.upload, name = "upload"),
    path("update/<int:song_id>", views.update, name = "update"),
    path("<int:song_id>", views.delete, name = "delete"),
    path("playlist_", views.playlist_, name = "playlist_"),
]
