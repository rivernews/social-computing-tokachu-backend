from django.shortcuts import render

from django.views.generic import TemplateView

from django.contrib.auth import get_user_model
from blog.models import (
    Post,
)
from rest_framework import viewsets
from .serializers import (
    PostSerializer,
)
from rest_framework import permissions
from rest_framework import serializers

class HomeView(TemplateView):
    template_name = "home.html"

home_view = HomeView.as_view()

class PostViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowOptionsIsAdminUserOrReadOnly,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # setup user upon creation, see https://stackoverflow.com/questions/32509815/django-rest-framework-get-data-from-foreign-key-relation
    user = serializers.PrimaryKeyRelatedField(
        # set it to read_only as we're handling the writing part ourselves
        read_only=True,
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)