from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
# Create your views here.
def index(request):
    context = {
    "students" : Students.objects.all()
    }
    return render(request, "pages/index.html", context)
