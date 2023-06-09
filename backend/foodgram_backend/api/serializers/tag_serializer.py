from rest_framework import serializers

from foodgram.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """
    Tag serializer.
    """
    class Meta:
        model = Tag
        fields = ("id", "name", "color", "slug")
