from django.contrib.auth import get_user_model

from rest_framework import viewsets
from .serializers import (
    UserSerializer
)
from rest_framework.decorators import action
from django.http import HttpResponse, JsonResponse
from .permission import AllowOptionsIsAdminUser

# from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = (AllowOptionsIsAdminUser,)

    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def log_in(self, request, pk=None):

        queryset = get_user_model().objects.filter(email=request.POST['email'])
        if queryset:
            pw = queryset.values()[0]['password']
            if pw == request.POST['password']:
                serializer = UserSerializer(queryset, many=True)
                return JsonResponse(serializer.data[0], status=201, safe=False)
            else:
                return JsonResponse({}, status=403, safe=False)
        else:
            return JsonResponse({}, status=404)