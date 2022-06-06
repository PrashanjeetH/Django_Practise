from rest_framework import serializers
from api.models import StudentsModel

# Create your models here.
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length=200)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    def create(self, validated_data):
        return StudentsModel.objects.create(**validated_data)