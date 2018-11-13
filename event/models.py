from django.db import models
from api.models import Pictures
from account.models import CustomUser
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=128)
    time = models.DateTimeField()
    place_id = models.CharField(max_length=64)
    owner_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
        )
    description = models.TextField()