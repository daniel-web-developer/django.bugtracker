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
        fields = ('title', 'description', 'priority', 'public')
        widgets = {
                "public": RadioSelect(),
                "priority": RadioSelect()
                }
        labels = {
                "public": "Tickets's privacy status"
                }

class editTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'priority', 'public', 'solved')
        widgets = {
                "public": RadioSelect(),
                "priority": RadioSelect(),
                "solved": RadioSelect()
                }
        labels = {
                "public": "Tickets's privacy status",
                "solved": "Is the ticket solved?"
                }
