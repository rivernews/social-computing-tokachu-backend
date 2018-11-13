from .models import (
    User_Event,
    Theme_Tag,
    Event_Picture,
    Interest_list,
    User_Conversation,
    Event_Tag
)
from rest_framework import serializers


class User_EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Event
        fields = "__all__"

class Theme_TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme_Tag
        fields = "__all__"

class Event_PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Picture
        fields = "__all__"

class Interest_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest_list
        fields = "__all__"

class User_ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Conversation
        fields = "__all__"

class Event_TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Tag
        fields = "__all__"
# class LocationSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Location
#         fields = '__all__'

# class TagSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Tag
#         fields = '__all__'


# class ThemeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Theme
#         fields = '__all__'