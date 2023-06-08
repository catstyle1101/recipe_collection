from django.db import models
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
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
    pagination_class = ProjectViewPagination
    action_serializer = ShortRecipeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilter

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
        # https://github.com/PyFPDF/fpdf2
        pass


