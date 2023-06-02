from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api.pagination import RecipeViewPagination
from foodgram.models import Recipe
from api.serializers import RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_filelds = ("name",)
    pagination_class = RecipeViewPagination