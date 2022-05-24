from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers import ProfileSerializer, UserSerialezer

from django.views.generic import UpdateView, CreateView

from core.forms import ProfileForm

from core.models import ProfileModel

class ProfileAPIView(APIView):
    def get(self, request):
        query_set = ProfileModel.objects.all()
        serializer = ProfileSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            print("Post data is valid")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class ProfileUpdateView(UpdateView):
    model = ProfileModel
    
class ProfileCreateView(CreateView):
    model = ProfileModel
    fields = ('__all__')
