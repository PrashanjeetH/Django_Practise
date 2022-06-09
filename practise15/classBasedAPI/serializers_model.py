from rest_framework import serializers


from classBasedAPI.models import StudentModel

#  Model Serializer here
class StudentSerializer(serializers.ModelSerializer):
    # Core arguments example to make name as read_only attribute
    # Method 1
    name = serializers.CharField(read_only=True, default='Default_name')

    class Meta:
        model = StudentModel
        # fields to be returned as response
        fields = ['name', 'roll_no', 'city']
        # Attributes to make it read_only property   
        # Method 2
        read_only_fields = ['name']

        # Method 3
        # extra_kwargs = {'name':{'read_only':True}}