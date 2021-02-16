from django.urls import path
from core.views import home, request_data

app_name='core'

# TODO: Remove Circular urls issue
urlpatterns = [
    path('', home, name = 'home'),
    path('request_data/', request_data, name = 'request_data')

]
