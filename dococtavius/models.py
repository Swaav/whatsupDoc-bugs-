from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Ticket(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=280)
    user_ticket = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='creator')
    time_date = models.DateTimeField(default=timezone.now)
    assigneduser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='bloodsign')
    completeuser = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='finisher')
    NEW = 'N'
    IN_PROGRESS = 'IP'
    DONE = 'D'
    INVALID = 'I'
    TICKET_STAT_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'IN Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid'),
    ]
    ticket_stats = models.CharField(
        max_length=180,
        choices=TICKET_STAT_CHOICES,
        default=NEW,
    )


    def __str__(self):
        return f"{self.title} - {self.user_ticket.name}"