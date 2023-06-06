from django.db import models
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from api.filters import RecipeFilter
from api.mixins import AddDelViewMixin
from api.pagination import ProjectViewPagination
from foodgram.models import Recipe, ShoppingCart
from api.serializers import RecipeSerializer
from foodgram.models.recipe import FavoriteRecipe
from users.serializers import ShortRecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet, AddDelViewMixin):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = RecipeFilter
    pagination_class = ProjectViewPagination
    action_serializer = ShortRecipeSerializer

    def get_queryset(self):
        query_tags = self.request.query_params.getlist("tags")
        query_is_favorited = self.request.query_params.get("is_favorited")
        if query_is_favorited:
            self.queryset = self.queryset.filter(
                in_favorites__user=self.request.user
            )
        if query_tags:
            self.queryset = self.queryset.filter(
                tags__slug__in=query_tags
            ).distinct()
        return self.queryset

    @action(
        methods=("GET", "POST", "DELETE"),
        detail=True,
        permission_classes=(IsAuthenticated,),
    )
    def favorite(self, request, pk):
        return self.add_del(pk, FavoriteRecipe, models.Q(recipe__id=pk))

    @action(
        methods=("GET", "POST", "DELETE"),
        detail=True,
        permission_classes=(IsAuthenticated,),
    )
    def shopping_cart(self, request, pk):
        return self.add_del(pk, ShoppingCart, models.Q(recipe__id=pk))

    @action(methods=("GET",), detail=False)
    def download_shopping_cart(self, request):
        pass
