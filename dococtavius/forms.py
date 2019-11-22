from django import forms
from . import models

class TicketAdd(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description',]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class EditForm(models.Form):
     class Meta:
        model = models.Ticket
        fields = ['title', 'description','ticket_stats', 'assigneduser']
