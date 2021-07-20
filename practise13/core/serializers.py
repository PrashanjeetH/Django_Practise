from rest_framework import serializers
from core.models import ProfileModel
from django.contrib.auth.models import User


class UserSerialezer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerialezer(read_only=True)
    class Meta:
        model = ProfileModel
        fields = ('user', 'contact', 'gender', 'bio')