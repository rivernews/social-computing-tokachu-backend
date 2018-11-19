from django.db import models
from api.models import Pictures, Theme
from account.models import CustomUser
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=128)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    place_id = models.CharField(max_length=64, null=True)
    owner_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
        )
    category = models.ForeignKey(
        Theme,
        on_delete=models.CASCADE
        )
    description = models.TextField()
