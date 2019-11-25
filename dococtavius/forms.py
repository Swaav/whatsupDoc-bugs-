from django import forms
from . import models
from .models import Ticket


class TicketAddForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'ticket_stats',
            'assigneduser'
        ]
        widgets = {
            'ticket': forms.RadioSelect
        }


form = TicketAddForm()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)



