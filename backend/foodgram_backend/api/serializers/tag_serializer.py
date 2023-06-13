from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from foodgram.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """
    Tag serializer.
    """
    class Meta:
        model = Tag
        fields = ("id", "name", "color", "slug")

    def validate(self, attrs):
        if Tag.objects.filter(color=attrs.get("color").upper()).exists():
            raise ValidationError("Цвет должен быть уникальным")
        if Tag.objects.filter(name=attrs.get("name").capitalize()).exists():
            raise ValidationError("Имя тега должно быть уникальным")
        if Tag.objects.filter(slug=attrs.get("slug").lower()).exists():
            raise ValidationError("Slug должен быть уникальным")
        return attrs
