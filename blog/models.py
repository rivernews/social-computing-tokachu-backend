from django.conf import settings
from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	
	user = models.ForeignKey(
        settings.AUTH_USER_MODEL, # or you can use '[from django.contrib.auth import get_user_model]' then get_user_model(). but only use these in models; you should use account.model.User anywhere else.
        null=True, # you have to use null=True since assigning user is difficult upon creation of this model. assign the author when creating an instance
        on_delete=models.SET_NULL
    )
	
	content = models.TextField(blank=True) # blank=True : not required column

	is_public = models.BooleanField(default=False)
	modified_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)