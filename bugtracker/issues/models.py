from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.urls import reverse
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    pass

class Project(models.Model):
    name = models.CharField(max_length=63)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(null=True, auto_now=True)
    project = models.OneToOneField(Project, blank=False, related_name="tickets")
