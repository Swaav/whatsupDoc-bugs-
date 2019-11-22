from django.db import models
from django.utils import timezone

class GhostPost(models.Model):
    ghostTitle = models.CharField(max_length=50)
    body = models.TextField(max_length=280)
    is_boast = models.BooleanField(default=False)
    post_date = models.DateTimeField(default=timezone.now)
    goodvote = models.IntegerField(default=0)
    badvote = models.IntegerField(default=0)
    totalvotes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ghostTitle} - {self.ghostAuthor.name}"