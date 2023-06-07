from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api.filters import TagFilter
from api.permissions import ReadOnly
from api.serializers import TagSerializer
from foodgram.models import Tag


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TagFilter
    filterset_filelds = ("name", "color", "slug")
    permission_classes = (ReadOnly,)
