
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
]

# client id
# 810685259512-7rhavrnfjvjgqahb8o7690bss99jdi96.apps.googleusercontent.com

# client secret id
# 89StvOiFHjpznhhUQyhGgeSf