import datetime
from django import forms
from .models import Project

from django.core.exceptions import ValidationError

class newProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'public')
