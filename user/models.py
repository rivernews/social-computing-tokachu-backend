from django.db import models
from picture.models import Picture
# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    picture_id = models.ForeignKey(
        Picture,
        null=True,
        on_delete=models.CASCADE
        )
    gender = models.IntegerField()
    age = models.IntegerField()
    description = models.TextField()
    date_joined = models.DateField(auto_now_add=True)

