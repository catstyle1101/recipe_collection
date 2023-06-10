from api.filters import TagFilter
from api.permissions import ReadOnly
from api.serializers import TagSerializer
from django_filters.rest_framework import DjangoFilterBackend
from foodgram.models import Tag
from rest_framework import viewsets


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset for paginated view of tags. may be filtered by query params:
    name, color, slug.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TagFilter
    filterset_filelds = ("name", "color", "slug")
    permission_classes = (ReadOnly,)
