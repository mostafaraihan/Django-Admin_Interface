from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    technology = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
