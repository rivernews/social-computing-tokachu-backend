from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.decorators import action
from django.http import HttpResponse, JsonResponse

#### Importing Models ####
from .models import (
    User_Event,
    Theme_Tag,
    Event_Picture,
    Interest_list,
    User_Conversation,
    Event_Tag
)

#### Importing Serializers ####
from .serializers import (
    User_EventSerializer,
    Theme_TagSerializer,
    Event_PictureSerializer,
    Interest_listSerializer,
    User_ConversationSerializer,
    Event_TagSerializer
)

class User_EventViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowOptionsIsAdminUserOrReadOnly,)

    queryset = User_Event.objects.all()
    serializer_class = User_EventSerializer
    
    @action(detail=True, methods=['get'])
    def get_events_by_user(self, request, pk=None):
        queryset = User_Event.objects.filter(user_id=pk)
        if queryset:
            serializer = User_EventSerializer(queryset, many=True)
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return JsonResponse({}, status=404)

    @action(detail=True, methods=['get'])
    def get_users_by_event(self, request, pk=None):
        queryset = User_Event.objects.filter(event_id=pk)
        if queryset:
            serializer = User_EventSerializer(queryset, many=True)
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return JsonResponse({}, status=404)

class Theme_TagViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowOptionsIsAdminUserOrReadOnly,)

    queryset = Theme_Tag.objects.all()
    serializer_class = Theme_TagSerializer
    
    @action(detail=True, methods=['get'])
    def get_tags_by_theme(self, request, pk=None):
        queryset = Theme_Tag.objects.filter(theme_id=pk)
        if queryset:
            serializer = Theme_TagSerializer(queryset, many=True)
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return JsonResponse({}, status=404)

class Event_PictureViewSet(viewsets.ModelViewSet):
    queryset = Event_Picture.objects.all()
    serializer_class = Event_PictureSerializer
    
    @action(detail=True, methods=['get'])
    def get_pictures_by_event(self, request, pk=None):
        queryset = Event_Picture.objects.filter(event_id=pk)
        if queryset:
            serializer = Event_PictureSerializer(queryset, many=True)
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return JsonResponse({}, status=404)

class Interest_listViewSet(viewsets.ModelViewSet):
    queryset = Interest_list.objects.all()
    serializer_class = Interest_listSerializer
    
    @action(detail=True, methods=['get'])
    def get_list_by_user(self, request, pk=None):
        queryset = Interest_list.objects.filter(user_id=pk)
        if queryset:
            serializer = Interest_listSerializer(queryset, many=True)
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return JsonResponse({}, status=404)

    @action(detail=True, methods=['get'])
    def get_interest_count(self, request, pk=None):
        queryset = Interest_list.objects.filter(event_id=pk)
        if queryset:
            return JsonResponse({'count': len(queryset)}, status=201, safe=False)
        else:
            return JsonResponse({}, status=404)


class User_ConversationViewSet(viewsets.ModelViewSet):
    queryset = User_Conversation.objects.all()
    serializer_class = User_ConversationSerializer
    
    @action(detail=True, methods=['get'])
    def get_conversations_by_user(self, request, pk=None):
        queryset = User_Conversation.objects.filter(user_id=pk)
        if queryset:
            serializer = User_ConversationSerializer(queryset, many=True)
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return JsonResponse({}, status=404)

    @action(detail=True, methods=['get'])
    def get_userList_by_conversation(self, request, pk=None):
        queryset = User_Conversation.objects.filter(conversation_id=pk)
        if queryset:
            serializer = User_ConversationSerializer(queryset, many=True)
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return JsonResponse({}, status=404)

class Event_TagViewSet(viewsets.ModelViewSet):
    queryset = Event_Tag.objects.all()
    serializer_class = Event_TagSerializer
    
    @action(detail=True, methods=['get'])
    def get_tags_by_event(self, request, pk=None):
        queryset = Event_Tag.objects.filter(event_id=pk)
        if queryset:
            serializer = Event_TagSerializer(queryset, many=True)
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return JsonResponse({}, status=404)

    @action(detail=True, methods=['get'])
    def get_events_by_tag(self, request, pk=None):
        queryset = Event_Tag.objects.filter(tag_id=pk)
        if queryset:
            serializer = Event_TagSerializer(queryset, many=True)
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return JsonResponse({}, status=404)
