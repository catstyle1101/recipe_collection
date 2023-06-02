from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api.serializers import IngredientSerializer
from foodgram.models import Ingredient


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_filelds = ("name",)
