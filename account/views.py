from django.contrib.auth import get_user_model

from rest_framework import viewsets
from .serializers import (
    UserSerializer
)

from .permission import AllowOptionsIsAdminUser

# from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (AllowOptionsIsAdminUser,)

    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
