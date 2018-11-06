from django.conf import settings
from django.db import models

class Pictures(models.Model):
    url_link = models.URLField(
        max_length=400
    )
    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL, # or you can use '[from django.contrib.auth import get_user_model]' then get_user_model(). but only use these in models; you should use account.model.User anywhere else.
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    description = models.TextField(
        blank=True,
        max_length=500
    )