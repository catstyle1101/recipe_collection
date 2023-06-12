from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from foodgram.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """
    Tag serializer.
    """
    color = serializers.SerializerMethodField()
    class Meta:
        model = Tag
        fields = ("id", "name", "color", "slug")

    def validate(self, data):
        if Tag.objects.filter(color=self.color.upper()).exists():
            raise ValidationError("Цвет должен быть уникальным")
        return data
