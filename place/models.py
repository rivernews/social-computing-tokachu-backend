from django.db import models
from picture.models import Picture

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=128)
    center_lat = models.FloatField()
    center_lon = models.FloatField()
    radius = models.FloatField()
    place_photo = models.ForeignKey(
        Picture,
        null=True,
        on_delete=models.CASCADE
        )
    description = models.TextField()

