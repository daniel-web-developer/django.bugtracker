import datetime
from django import forms
from .models import Project
from django.forms import RadioSelect

from django.core.exceptions import ValidationError

PRIVACY_OPTIONS = ["Yes", "No"]

class newProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'public')
        widgets = {
            "public": RadioSelect()
        }
