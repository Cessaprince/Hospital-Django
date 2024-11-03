
from django.db import models

# Create your models here.

"""This model is for the appointment form part of the page."""


class Patient(models.Model):
    first_name = models.CharField(max_length=10, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    email = models.EmailField()
    addressline1 = models.TextField('Chevron',max_length=100)
    addressline2 = models.TextField(max_length=100, null=True, blank=True)
    phone = models.IntegerField()