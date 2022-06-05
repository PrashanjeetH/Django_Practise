from rest_framework import serializers

from drf2.models import StudentsModel

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return StudentsModel.objects.create(**validated_data)