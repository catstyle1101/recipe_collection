from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api.filters import IngredientFilter
from api.permissions import ReadOnly
from api.serializers import IngredientSerializer
from foodgram.models import Ingredient


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset for paginated view of Ingredients. May be filtered
    by query param name.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IngredientFilter
    filterset_fields = ("name",)
    permission_classes = (ReadOnly,)
