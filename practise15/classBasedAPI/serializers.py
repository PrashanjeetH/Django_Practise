from rest_framework import serializers
from classBasedAPI.models import StudentModel
# Validators
def starts_with_capitals(value):
    if not value[0].isupper():
        raise serializers.ValidationError('Name should start with capital letter only!')
    return value

def check_for_valid_name(value):
    if not (''.join(value.split())).isalpha():
        raise serializers.ValidationError('Name should not contain any numbers!')
    return value


# Create your models here.
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[starts_with_capitals, check_for_valid_name])
    # name = serializers.CharField(max_length=100)
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length=200)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    def create(self, validated_data):
        return StudentModel.objects.create(**validated_data)

    # Field level Validation for roll attribute
    # SYNTAX: def validate_fieldname(self, value):
    # def validate_roll_no(self, value):
    #     if value > 999 and value < 100:
    #         raise serializers.ValidationError(f'Roll number `{value}` is out of range!')
    #     return value

    # Object level validation for whole object attributes
    # def validate(self, data):
    #     name = data.get('name')
    #     roll_no = int(data.get('roll_no'))
    #     city = data.get('city')
    #     # do not allows an entry with below object values
    #     if name.lower() == 'jeetu' and roll_no == 105 and city.lower() == 'nagpur':
    #         raise serializers.ValidationError("Special Case! this combination of entry is not allowed.")
    #     return data