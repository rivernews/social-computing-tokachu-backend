from django.conf import settings
from django.db import models
from event.models import Event
from django.contrib.auth import get_user_model
from api.models import Theme
from api.models import Tag
from api.models import Pictures
from conversation.models import Conversation

class User_Event(models.Model):
    event_id = models.ForeignKey(
        Event,
        null=True,
        on_delete=models.SET_NULL
        )
    user_id = models.ForeignKey(
        get_user_model(), # or you can use '[from django.contrib.auth import get_user_model]' then get_user_model(). but only use these in models; you should use account.model.User anywhere else.
        null=True,
        on_delete=models.SET_NULL
    ) 
    state = models.IntegerField() #0 for past, 1 for future

class Theme_Tag(models.Model):
    theme_id = models.ForeignKey(
        Theme,
        on_delete=models.CASCADE
        )
    tag_id = models.ForeignKey(
        Tag, # or you can use '[from django.contrib.auth import get_user_model]' then get_user_model(). but only use these in models; you should use account.model.User anywhere else.
        on_delete=models.CASCADE
    ) 

class Event_Picture(models.Model):
    event_id = models.ForeignKey(
        Event,
        null=True,
        on_delete=models.SET_NULL
        )
    
    picture_id = models.ForeignKey(
        Pictures,
        null=True,
        on_delete=models.SET_NULL
    )


class Interest_list(models.Model):
    event_id = models.ForeignKey(
        Event,
        null=True,
        on_delete=models.SET_NULL
        )
    user_id = models.ForeignKey(
        get_user_model(), # or you can use '[from django.contrib.auth import get_user_model]' then get_user_model(). but only use these in models; you should use account.model.User anywhere else.
        null=True,
        on_delete=models.SET_NULL
    ) 

class User_Conversation(models.Model):
    user_id = models.ForeignKey(
        get_user_model(), # or you can use '[from django.contrib.auth import get_user_model]' then get_user_model(). but only use these in models; you should use account.model.User anywhere else.
        null=True,
        on_delete=models.SET_NULL
    ) 
    conversation_id = models.ForeignKey(
        Conversation,
        null=True,
        on_delete=models.SET_NULL
    ) 

class Event_Tag(models.Model):
    event_id = models.ForeignKey(
        Event,
        null=True,
        on_delete=models.SET_NULL
        )
    tag_id = models.ForeignKey(
        Tag, # or you can use '[from django.contrib.auth import get_user_model]' then get_user_model(). but only use these in models; you should use account.model.User anywhere else.
        null=True,
        on_delete=models.SET_NULL
    )
