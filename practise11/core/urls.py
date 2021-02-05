from django.urls import path
from core.views import home, Name


urlpatterns = [
    path('', home.as_view(), name = 'home')
    # path('', Name, name = 'home')
]
