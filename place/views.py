from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from place.models import Place
from place.serializers import PlaceSerializer
from django.http import HttpResponse, JsonResponse

# Create your views here.
class PlaceViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowOptionsIsAdminUserOrReadOnly,)

    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def retrieve(self, request, pk=None):
        queryset = Place.objects.filter(pk=pk)
        if queryset:
            serializer = PlaceSerializer(queryset, many=True)
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return JsonResponse({}, status=404)
    def perform_create(self, serializer):
        serializer.save()

    