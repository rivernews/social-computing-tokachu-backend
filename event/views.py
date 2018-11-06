from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from .models import Event
from .serializers import EventSerializer
from django.http import HttpResponse, JsonResponse
from conversation.serializers import ConversationSerializer


# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowOptionsIsAdminUserOrReadOnly,)

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def retrieve(self, request, pk=None):
        queryset = Event.objects.filter(pk=pk)
        if queryset:
            serializer = EventSerializer(queryset, many=True)
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return JsonResponse({}, status=404)

    def perform_create(self, serializer):
        # create a conversation here
        new_event = serializer.save()
        print(new_event.id)
        con = ConversationSerializer(data={"event_id": new_event.id, "group": 1})
        if con.is_valid():
            con.save()


    