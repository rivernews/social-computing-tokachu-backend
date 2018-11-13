from rest_framework import viewsets
from rest_framework import serializers

#### Importing Models ####
from .models import (
    Pictures,
    Location,
    Tag,
    Theme
)

#### Importing Serializers ####
from .serializers import (
    PicturesSerializer,
    LocationSerializer,
    TagSerializer,
    ThemeSerializer
)

class PicturesViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowOptionsIsAdminUserOrReadOnly,)

    queryset = Pictures.objects.all()
    serializer_class = PicturesSerializer

    # setup user upon creation, see https://stackoverflow.com/questions/32509815/django-rest-framework-get-data-from-foreign-key-relation
    uploader = serializers.PrimaryKeyRelatedField(
        # set it to read_only as we're handling the writing part ourselves
        read_only=True,
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LocationViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowOptionsIsAdminUserOrReadOnly,)

    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class TagViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowOptionsIsAdminUserOrReadOnly,)

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer