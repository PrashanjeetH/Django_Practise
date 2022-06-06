from urllib import response
from itsdangerous import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from api.models import StudentsModel
from api.serializers import StudentSerializer


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def students_list(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            try:
                student = StudentsModel.objects.get(pk=id)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({'detail': 'No valid input found.'}, status=status.HTTP_400_BAD_REQUEST)
        students = StudentsModel.objects.all()  
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'detail': 'Entry Created!'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'detail': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'PUT':
        id = request.data.get('id')
        query = StudentsModel.objects.filter(pk=id)
        if id is not None and query.exists():
            serializer = StudentSerializer(query[0], data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'detail': 'Data Updated'}, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
        return Response({'detail': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method =='DELETE':
        id = request.data.get('id')
        query = StudentsModel.objects.filter(pk=id)
        if id is not None and query.exists():
            query[0].delete()
            return Response({'detail': 'Data Deleted'}, status=status.HTTP_200_OK)