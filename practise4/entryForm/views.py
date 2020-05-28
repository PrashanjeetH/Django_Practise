from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Form
# create your views here

def index(request):
    context = {
        "details" : Form.objects.all()
    }
    return render(request, "pages/index.html", context)

def page1(request):
    return HttpResponse("pouiygbnjkl")
