from django.db import models
from event.models import Event
# Create your models here.
class Conversation(models.Model):
    channel_name = models.CharField(max_length=128, null=True)
    event_id = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
        )
    group = models.IntegerField()
