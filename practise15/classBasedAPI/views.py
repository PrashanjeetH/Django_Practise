from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


from classBasedAPI.models import StudentModel
from classBasedAPI.serializers import StudentSerializer

class StudentAPIView(APIView):
    
    
    def get(self, requests, format=None):
        id = requests.data.get('id')
        if id is not None:
            try:
                student = StudentModel.objects.get(pk=id)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({'detail': 'No valid input found.'}, status=status.HTTP_400_BAD_REQUEST)
        students = StudentModel.objects.all()  
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'detail': 'Entry Created!'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'detail': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, format=None):
        id = request.data.get('id')
        query = StudentModel.objects.filter(pk=id)
        if id is not None and query.exists():
            serializer = StudentSerializer(query[0], data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'detail': 'Data Updated'}, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
        return Response({'detail': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, format=None):
            id = request.data.get('id')
            query = StudentModel.objects.filter(pk=id)
            if id is not None and query.exists():
                serializer = StudentSerializer(query[0], data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'detail': 'Data Updated'}, status=status.HTTP_202_ACCEPTED)
                return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
            return Response({'detail': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, format=None):
        id = request.data.get('id')
        query = StudentModel.objects.filter(pk=id)
        if id is not None and query.exists():
            query[0].delete()
            return Response({'detail': 'Data Deleted'}, status=status.HTTP_200_OK)
