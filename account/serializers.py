from django.contrib.auth import get_user_model
from rest_framework import serializers

def get_field_name_list(model_object):
    return [ field_obj.name for field_obj in model_object._meta.fields ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = get_user_model()
        fields = get_field_name_list(get_user_model())
        # fields = ('email','id')