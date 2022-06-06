import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


from api.models import StudentsModel
from api.serializers_model import StudentSerializer


# Function Based APIView

@csrf_exempt
def students_list(request):
    if request.method =='GET':
        received_data = request.body
        stream = io.BytesIO(received_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            student_data = StudentsModel.objects.get(id=1)
            serializer =  StudentSerializer(student_data)
            return JsonResponse(serializer.data)
        students = StudentsModel.objects.all()
        # NOTE: When passing python object to a serializer with data argument you have to call .is_valid() method or else 
        # use serializer.initial_data to access the serialized data
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)


    elif request.method =='POST':
        received_data = request.body
        stream = io.BytesIO(received_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            # TODO: Try a method to append message with the serialized data itself
            # serializer.update({'message':'Provided student data uploaded successfully.'})
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


    elif request.method == 'PUT':
        received_data = request.body
        stream = io.BytesIO(received_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        id = python_data.get('id')
        student = StudentsModel.objects.get(id=id)
        serializer = StudentSerializer(student, data=python_data)   # add argument partial=True for partially updating the entry
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        received_data = request.body
        stream = io.BytesIO(received_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        try:
            student_data = StudentsModel.objects.get(id=id)
            serializer =  StudentSerializer(student_data)
            student_data.delete()
            return JsonResponse(serializer.data)
        except ObjectDoesNotExist:
            return JsonResponse({'message':f'No Entry Found with id = {id}'}, safe=False)
    # If requested HTTP method is not one of GET, POST, PUT, DELETE
    return JsonResponse({'message':'Invalid request. Method Not Allowed.'}, safe=False)


# Class Based APIView

from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPIView(View):
    def get(self, request, *args, **kwargs):
        # logic for handelling GET request to retrive data
        pass
    def post(self, request, *args, **kwargs):
        # logic for handelling POST request to receive data
        pass
    def put(self, request, *args, **kwargs):
        # logic for handelling PUT request to update data (full/partial)
        pass
    def delete(self, request, *args, **kwargs):
        # logic for handelling DELETE request to delete data
        pass
    