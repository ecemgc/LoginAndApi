from django.db import models
from datetime import datetime

from employees.models import Employee
from departments.models import Department

from .enums import ApprovalStatus

class Demand(models.Model):
    sender_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='sender_employee')
    #kimin epartmanı olacak burada
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True,)
    #talep türü choice olmalı 
    demand_type = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=datetime.now)
    demand_message = models.CharField(max_length=250)
    document = models.ImageField(null=True)
    approver_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='approver_employee')
    receiver_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='receiver_employee')
    approval_status = models.CharField(max_length=100, choices=ApprovalStatus.choices(), null=True)
    approver_approval_status = models.CharField(max_length=100, choices=ApprovalStatus.choices(), null=True)
    receiver_approval_status = models.CharField(max_length=100, choices=ApprovalStatus.choices(), null=True)
    note = models.TextField(max_length=250)
    
    

    
    