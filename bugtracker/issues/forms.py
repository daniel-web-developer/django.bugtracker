import datetime
from django import forms
from .models import Project, Ticket
from django.forms import RadioSelect

from django.core.exceptions import ValidationError

class newProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'public')
        widgets = {
            "public": RadioSelect()
        }
        labels = {
            "public": "Project's privacy status"
        }

class newTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'public')
        widgets = {
            "public": RadioSelect()
        }
        labels = {
            "public": "Tickets's privacy status"
        }
