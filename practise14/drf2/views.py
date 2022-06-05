from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt


from drf2.models import StudentsModel
from drf2.serializers import StudentSerializer

# Create your views here.
def student_detail(request, pk):
    student = StudentsModel.objects.get(id=pk)

    # Method 1
    serializer = StudentSerializer(student)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')


def student_list(request):
    student = StudentsModel.objects.all()
    serializer = StudentSerializer(student, many=True)

    # Method 2
    return JsonResponse(serializer.data, safe=False)

# # Method 1
# @csrf_exempt     # To bypass the Django csrf validation
# def student_create(request):
#     if request.method =='POST':
#         received_data = request.body
#         stream = io.BytesIO(received_data)
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             msg = {"Response": "Student data inserted successfuly!"}
#             json_response = JSONRenderer().render(msg)
#             return HttpResponse(json_response, content_type = 'application/json')
#         return HttpResponse(JSONRenderer().render(serializer.errors), content_type = 'application/json')
#     return HttpResponse(JSONRenderer().render({'Response':'Method Not Allowed.'}), content_type = 'application/json')


# Method 2
@csrf_exempt     # To bypass the Django csrf validation 
def student_create(request):
    if request.method =='POST':
        received_data = request.body
        print(received_data, end='\n\n\n\n\n')
        stream = io.BytesIO(received_data)
        print(stream, end='\n\n\n\n')
        python_data = JSONParser().parse(stream)
        print(python_data)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            response = {"Response": "Student data inserted successfuly!"}
            return JsonResponse(response)
        return JsonResponse(serializer.errors)
    return JsonResponse({'Response':'Method Not Allowed.'})