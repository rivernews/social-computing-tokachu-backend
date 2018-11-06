from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from .models import Conversation
from .serializers import ConversationSerializer
from django.http import HttpResponse, JsonResponse


# Create your views here.
class ConversationViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowOptionsIsAdminUserOrReadOnly,)

    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def retrieve(self, request, pk=None):
        queryset = Conversation.objects.filter(pk=pk)
        if queryset:
            serializer = ConversationSerializer(queryset, many=True)
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return JsonResponse({}, status=404)

    def perform_create(self, serializer):
        new_conversation = serializer.save()
        

    