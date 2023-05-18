from rest_framework import serializers
from common.common_enum import Status
from departments.models import Department

from employees.enums import Gender
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ()    

class CreateEmployeeSerializer(serializers.Serializer):

    status = serializers.ChoiceField(required=True, choices=Status.get_values())
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    gender = serializers.ChoiceField(choices=Gender.get_values() ,required=True)
    birth_date = serializers.DateField(required=False, allow_null=True)
    position = serializers.CharField(required=True)
    start_date = serializers.DateField(required=False, allow_null=True)
    picture = serializers.ImageField(required=False, allow_null=True)
    join_date = serializers.DateField(required=False, allow_null=True)
    note = serializers.CharField(required=True)
    department = serializers.IntegerField(required=True)

    def validate(self, attrs):
        attrs['username'] = "{}_{}".format(attrs['first_name'], attrs['last_name'])
        attrs['password'] = "{}.{}123!".format(attrs['first_name'], attrs['last_name'])
        return attrs
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)