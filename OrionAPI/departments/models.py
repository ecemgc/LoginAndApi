from django.db import models

class Department(models.Model):

    name = models.CharField(max_length=50)
    note = models.TextField(max_length=250)

    def __str__(self):
        return self.name