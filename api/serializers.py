from .models import (
    Pictures,
    Location,
    Tag,
    Theme
)
from rest_framework import serializers


class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'