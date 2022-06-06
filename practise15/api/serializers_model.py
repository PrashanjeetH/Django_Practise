from email.policy import default
from rest_framework import serializers


from api.models import StudentsModel

#  Model Serializer here
class StudentSerializer(serializers.ModelSerializer):
    # Core arguments example to make name as read_only attribute
    # Method 1
    name = serializers.CharField(read_only=True, default='Default_name')

    class Meta:
        model = StudentsModel
        # fields to be returned as response
        fields = ['name', 'roll_no', 'city']
        # Attributes to make it read_only property   
        # Method 2
        read_only_fields = ['name']

        # Method 3
        # extra_kwargs = {'name':{'read_only':True}}