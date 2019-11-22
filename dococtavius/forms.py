from django import forms
from . import models

class TicketAdd(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description',]
