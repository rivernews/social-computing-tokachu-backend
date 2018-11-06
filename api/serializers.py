from .models import Pictures
from rest_framework import serializers


class PicturesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pictures
        fields = "__all__"