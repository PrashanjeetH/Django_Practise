#Django Built-in

from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.contrib.auth.hashers import make_password, check_password

# Own

from .models import Signupmodel
from .forms import Signupform, Loginform

# Create your views here.

def index(request):
    return render(request, "pages/index.html")


def signup(request):
    context = {}
    form_content = Signupform()
    if request.method == 'POST':
        form_content = Signupform(request.POST)
        if form_content.is_valid():
            # cleaned_data helps in formating raw data of form, it returns the form data in dict format
            data = form_content.cleaned_data
            # make_password converts your raW password in hash, by defaut in pbkdf2_sha256
            data['password'] = make_password(data['password'])
            # double pointer denotesof passing the dict as arguement to map proeperly the form with the models
            Signupmodel.objects.create(**data)
            form_content = Signupform()
    context['form'] = form_content
    return render(request, "pages/signup.html", context )


def login(request):
    context = {}
    credit = Loginform()
    if request.method == "POST":
        credit = Loginform(request.POST)

        if credit.is_valid():
            data = credit.cleaned_data
            db_data = Signupmodel.objects.get(fname = data['username'])
            if db_data.fname == data['username'] and check_password(data['password'], db_data.password):
                return render(request, "pages/loggedin.html", context)
            else:
                return HttpResponse("Not an authentic user")
    context['data'] = credit
    return render(request, "pages/login.html", context)


def loggedin(request):
    return render(request, "pages/loggedin.html")
