from rest_framework import serializers
from core.models import ProfileModel
from django.contrib.auth.models import User
from core.models import ProfileModel


class UserSerialezer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerialezer(read_only=True)
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    def create(self, validated_data):
        print(validated_data)
        user_dict = validated_data.pop('user')
        user_obj, created = User.objects.get_or_create(**user_dict)
        return ProfileModel.objects.create(user=user_obj, **validated_data)

    class Meta:
        model = ProfileModel
        fields = ('user', 'contact', 'gender', 'bio')