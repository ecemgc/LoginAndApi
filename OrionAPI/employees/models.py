from model_utils import Choices
from django.db import models
from .enums import Gender
from datetime import datetime
from model_utils.models import StatusModel
from common.common_enum import Status
from departments.models import Department
from django.contrib.auth.models import AbstractUser
  
class Employee(AbstractUser):

    status = models.CharField(max_length=15, choices=Status.choices(), default=Status.ACTIVE.value)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=10, choices=Gender.choices(), default=Gender.UNKNOWN.value)
    birth_date = models.DateField(null=True)
    email = models.EmailField(max_length=250, null=True, unique=True)
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    start_date = models.DateField(null=True)
    picture = models.ImageField(null=True)
    join_date = models.DateField(default=datetime.now)
    note = models.TextField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True, null=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    



