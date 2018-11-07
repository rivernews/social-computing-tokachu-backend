from django.contrib.auth import get_user_model
from .models import Conversation
from rest_framework import serializers
import random
import string

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'
    
    def create(self, validated_data):

        conversation = Conversation(
            channel_name=generate_random_string(64),
            event_id = validated_data['event_id'],
            group = validated_data['group'])
        conversation.save()
        return conversation

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
