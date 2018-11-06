from django.db import models
from api.models import Pictures

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=64)
    min_lat = models.FloatField()
    max_lat = models.FloatField()
    min_lon = models.FloatField()
    max_lon = models.FloatField()
    place_photo = models.ForeignKey(
        Pictures,
        null=True,
        on_delete=models.CASCADE
        )
    description = models.TextField()

