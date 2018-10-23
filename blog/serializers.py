from django.contrib.auth import get_user_model
from blog.models import Post
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    # see https://stackoverflow.com/questions/32509815/django-rest-framework-get-data-from-foreign-key-relation
    author_full_name = serializers.CharField(source='user', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'