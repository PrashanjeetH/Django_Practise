from django.shortcuts import render
from core.models import StudentModel
from django.http import JsonResponse
# Create your views here.


def request_data(request):
    object = StudentModel.objects.all()
    return JsonResponse(object, safe=False)

def home(request):
    return render(request, 'core/home.html', context={
            'title': "Home Page"
                    })
