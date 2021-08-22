from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


# Create your models
class Resume(models.Model):
    firstname = models.CharField(max_length=20, blank=True, null=True)
    othername = models.CharField(max_length=20, blank=True, null=True)
    Surname = models.CharField(max_length=20, blank=True, null=True)
    age = models.PositiveIntegerField()
    skills = models.TextField(blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)
    Address = models.TextField(blank=True, null=True)
    email = models.URLField(blank=True, null=True)
    education = models.TextField(blank=True)
    Experience = models.TextField(blank=True, null=True)
    cv = models.FileField(blank=True, null=True, upload_to='uploads/')


