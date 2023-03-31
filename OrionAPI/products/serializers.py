from rest_framework import serializers
from departments.models import Department

from employees.models import Employee

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    department_id = serializers.StringRelatedField()
    employee_id = serializers.StringRelatedField()


    class Meta:
        model = Product
        exclude = ()

class CreateProductSerializer(serializers.Serializer):
    brand = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    category = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=False, allow_null=True)
    buy_at = serializers.DateTimeField(required=False, allow_null=True)
    bill_image = serializers.ImageField(required=False, allow_null=True)
    asset_status = serializers.CharField(required=True)
    note = serializers.CharField(required=True)
    employee_id = serializers.IntegerField(required=True)
    department_id = serializers.IntegerField(required=True)

    def createEmp(self, validated_data):
        employee_name = validated_data.pop('employee_id')
        employee = Employee.objects.get(first_name=employee_name)
        product = Product.objects.create(product=employee, **validated_data)
        return product
    #yap
    def createDep(self, validated_data):
        department_name = validated_data.pop('department_id')
        department = Department.objects.get(name=department_name)
        employee = Employee.objects.create(department=department, **validated_data)
        return employee
    #yap
    
class UpdateProductSerializer(serializers.Serializer):
    brand = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    category = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=False, allow_null=True)
    buy_at = serializers.DateTimeField(required=False, allow_null=True)
    bill_image = serializers.ImageField(required=False, allow_null=True)
    asset_status = serializers.CharField(required=True)
    note = serializers.CharField(required=True)
    employee_id = serializers.IntegerField(required=False)
    department_id = serializers.IntegerField(required=False)