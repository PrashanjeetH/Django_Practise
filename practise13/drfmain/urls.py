
from django.contrib import admin
from django.urls import path
from core.views import ProfileAPIView, ProfileUpdateView, ProfileCreateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ProfileAPIView.as_view(), name='profiles'),
    path('update/<int:pk>',ProfileUpdateView.as_view(), name='update_profile'),
    path('create',ProfileCreateView.as_view(), name='create_profile'),
]
