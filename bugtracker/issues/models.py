from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.conf import settings
from django.forms import ModelForm

# Create your models here.
class User(AbstractUser):
    pass

PRIVACY_OPTIONS = ((True, "Public"), (False, "Private"))
SOLVED_OPTIONS = ((True, "Solved"), (False, "Not solved"))
PRIORITY_OPTIONS = (
    (0, "Low priority"),
    (1, "Medium priority"),
    (2, "High priority")
)

class Project(models.Model):
    name = models.CharField(max_length=63)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    public = models.BooleanField(default=False, choices=PRIVACY_OPTIONS)
    permalink = models.CharField(max_length = 10, unique=True)
    
    def __str__(self):
        return self.author.username

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    edited_on = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey(Project, blank=False, related_name="tickets", on_delete=models.CASCADE)
    public = models.BooleanField(default=False, choices=PRIVACY_OPTIONS)
    priority = models.SmallIntegerField(default="0", choices=PRIORITY_OPTIONS)
    solved = models.BooleanField(default=False, choices=SOLVED_OPTIONS)
    permalink = models.CharField(max_length = 10, unique=True)

    class Meta:
        ordering = ['-created_on', 'solved']

    def __str__(self):
        return self.title

