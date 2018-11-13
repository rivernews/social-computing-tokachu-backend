from .models import (
    Pictures,
    Location,
    Tag,
    Theme
)
from rest_framework import serializers


class PicturesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pictures
        fields = "__all__"

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'