from django.db import models

# Create your models here.

class Teacher(models.Model):
    fullname = models.CharField(max_length=100)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=12)
    address = models.CharField(max_length=100)

    # CRED operarion when teacher enters the details of students





