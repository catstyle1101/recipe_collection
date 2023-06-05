from django_filters import rest_framework as filters
from rest_framework import viewsets

from api.filters import RecipeFilter
from api.pagination import ProjectViewPagination
from foodgram.models import Recipe
from api.serializers import RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RecipeFilter
    pagination_class = ProjectViewPagination