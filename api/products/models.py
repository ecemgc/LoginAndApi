from django.db import models
from employees.models import Employee
from departments.models import Department
from datetime import datetime

class Product(models.Model):

    brand = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=datetime.now, null=True)
    buy_at = models.DateTimeField(null=True)
    bill_image = models.ImageField(null=True)
    asset_status = models.CharField(max_length=250)
    note = models.CharField(max_length=250)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

