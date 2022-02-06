from enum import Flag
from django.db import models

# Create your models here.

class Eoi(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    
    email = models.EmailField()
    gender = models.CharField(max_length=255, blank=False, null=True, choices=GENDER)
    phone = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=False)
    level_of_education = models.CharField(max_length=255, blank=False)
    