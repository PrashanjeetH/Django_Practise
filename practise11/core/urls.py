from django.urls import path
from core.views import home, Name, PassCheck


urlpatterns = [
    path('', home.as_view(), name = 'home'),
    # path('', Name, name = 'home')
    path('number-of-visits/', PassCheck.as_view(), name = "passcheck"),
]
