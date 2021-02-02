from django.urls import path
from core.views import home


urlpatterns = [
    path('', home.as_view(), name = 'home')
]
