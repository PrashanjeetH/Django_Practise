#Django Built-in
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.hashers import make_password, check_password

# Own

from .models import Signupmodel
from .forms import Signupform

# Create your views here.

def index(request):
    return render(request, "pages/index.html")

def signup(request):
    context = {}
    form_content = Signupform()
    if request.method == 'POST':
        form_content = Signupform(request.POST)
        if form_content.is_valid():
            data = form_content.cleaned_data
            data['password'] = make_password(data['password'])
            Signupmodel.objects.create(**data)
            form_content = Signupform()
    context['form'] = form_content
    return render(request, "pages/signup.html", context )
