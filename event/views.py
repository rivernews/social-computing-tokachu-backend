from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from .models import Event
from .serializers import EventSerializer
from django.http import HttpResponse, JsonResponse
from conversation.serializers import ConversationSerializer
from connection.serializers import User_ConversationSerializer
from rest_framework.decorators import action
from datetime import datetime
from datetime import timezone


# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowOptionsIsAdminUserOrReadOnly,)

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def retrieve(self, request, pk=None):
        if not pk:
            print("here")
        queryset = Event.objects.filter(pk=pk)
        if queryset:
            serializer = EventSerializer(queryset, many=True)
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return JsonResponse({}, status=404)

    def perform_create(self, serializer):
        # create a conversation here
        new_event = serializer.save()
        con = ConversationSerializer(data={"event_id": new_event.id, "group": 1})

        if con.is_valid():
            newCon = con.save()
            user_con = User_ConversationSerializer(data={"user_id": new_event.owner_id.id, "conversation_id": newCon.id})
            if user_con.is_valid():
                user_con.save()

    @action(detail=False, methods=['get'])
    def search(self, request):
        dateFormatter = "%Y-%m-%d %H:%M"
        categories = (request.GET['category']).split(",")
        start_time = datetime.strptime(request.GET['start_time'], dateFormatter).replace(tzinfo=timezone.utc)
        end_time = datetime.strptime(request.GET['end_time'], dateFormatter).replace(tzinfo=timezone.utc)
        print(categories)
        print(start_time)
        print(end_time)
        queryset = Event.objects.filter(start_time__range=(start_time, end_time)).filter(category__in=categories)
        if queryset:
            serializer = EventSerializer(queryset, many=True)
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return JsonResponse({}, status=404)

    