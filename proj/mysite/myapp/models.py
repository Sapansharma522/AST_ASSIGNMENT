# models.py
from django.db import models

class Job(models.Model):
    company = models.CharField(max_length=255)
    extractedSalary = models.IntegerField()  # Assuming extractedSalary is an integer field
    title = models.CharField(max_length=255)
    jobLocationCity = models.CharField(max_length=255)

