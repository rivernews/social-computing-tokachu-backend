from rest_framework import viewsets
from rest_framework import serializers

#### Importing Models ####
from .models import Pictures

#### Importing Serializers ####
from .serializers import PicturesSerializer

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