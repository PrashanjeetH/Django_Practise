"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import UserDataForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('userData')

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request,
                          template_name="app/register.html",
                          context={'form': form})

    form = UserCreationForm
    return render(request,
                  template_name="app/register.html",
                  context={'form': form,
                           'title': "Sign Up",
                           'year':  datetime.now().year})


def userData(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            for message in form.errors:
                print(message)
            return render(request, template_name='app/user_detail.html', context={'form': form,
                                                                                  'title': "Sign Up",
                                                                                  'year': datetime.now().year})
    form = UserDataForm()
    return render(request, template_name='app/user_detail.html', context={'form': form,
                                                                          'title': "Sign Up",
                                                                          'year': datetime.now().year})
