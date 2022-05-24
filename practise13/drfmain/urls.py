
from django.contrib import admin
from django.urls import path
from core.views import ProfileAPIView, ProfileUpdateView, ProfileCreateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles',ProfileAPIView.as_view(), name='profiles'),
    path('profile/<int:pk>',ProfileUpdateView.as_view(), name='profile'),
    path('create',ProfileCreateView.as_view(), name='create_profile'),
]
