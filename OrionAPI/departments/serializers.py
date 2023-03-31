from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        exclude = ()

class CreateDepartmentSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    note = serializers.CharField(required=True)
    