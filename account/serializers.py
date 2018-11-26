from django.contrib.auth import get_user_model
from rest_framework import serializers

from django.contrib.auth.hashers import make_password

def get_field_name_list(model_object):
    return [ field_obj.name for field_obj in model_object._meta.fields ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    def validate_password(self, value: str) -> str:
        return make_password(value)
    
    class Meta:
        model = get_user_model()
        fields = get_field_name_list(get_user_model())