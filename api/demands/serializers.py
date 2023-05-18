from rest_framework import serializers
from .models import Demand
from .enums import ApprovalStatus

class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        exclude = ()

class CreateDemandSerializer(serializers.Serializer):
    sender_employee_id = serializers.IntegerField(required=True)
    department_id = serializers.IntegerField(required=True)
    demand_type =  serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=False, allow_null=True)
    demand_message = serializers.CharField(required=True)
    document = serializers.ImageField(required=False, allow_null=True)
    approver_employee_id = serializers.IntegerField(required=True)
    receiver_employee_id = serializers.IntegerField(required=True)
    approval_status = serializers.ChoiceField(choices=ApprovalStatus.get_values(), required=False, allow_null=True)
    approver_status = serializers.ChoiceField(choices=ApprovalStatus.get_values(), required=False, allow_null=True)
    receiver_status = serializers.ChoiceField(choices=ApprovalStatus.get_values(), required=False, allow_null=True)
    note = serializers.CharField(required=True)

class UpdateDemandSerializer(serializers.Serializer):
    sender_employee_id = serializers.IntegerField(required=False)
    department_id = serializers.IntegerField(required=False)
    demand_type =  serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=False, allow_null=True)
    demand_message = serializers.CharField(required=True)
    document = serializers.ImageField(required=False, allow_null=True)
    approver_employee_id = serializers.IntegerField(required=False)
    receiver_employee_id = serializers.IntegerField(required=False)
    approval_status = serializers.ChoiceField(choices=ApprovalStatus.get_values(), required=False, allow_null=True)
    approver_status = serializers.ChoiceField(choices=ApprovalStatus.get_values(), required=False, allow_null=True)
    receiver_status = serializers.ChoiceField(choices=ApprovalStatus.get_values(), required=False, allow_null=True)
    note = serializers.CharField(required=True)
