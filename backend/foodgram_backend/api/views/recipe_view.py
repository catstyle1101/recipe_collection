import csv

from api.filters import RecipeFilter
from api.mixins import AddDelViewMixin
from api.pagination import ProjectViewPagination
from api.serializers import RecipeSerializer
from django.db import models
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from foodgram.models import IngredientRecipe, Recipe, ShoppingCart
from foodgram.models.recipe import FavoriteRecipe
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from users.serializers import ShortRecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet, AddDelViewMixin):
    """
    Viewset for paginated view of recipes.
    """
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
    def favorite(self, _, pk: int | str) -> Response:
        """
        Add or delete Recipe to m2m relation with User
        through FavoriteRecipe model.
        """
        return self.add_del(pk, FavoriteRecipe, models.Q(recipe__id=pk))

    @action(
        methods=("GET", "POST", "DELETE"),
        detail=True,
        permission_classes=(IsAuthenticated,),
    )
    def shopping_cart(self, _, pk: int | str) -> Response:
        """
        Add or delete Recipe to m2m relation with User through
        ShoppingCart model.
        """
        return self.add_del(pk, ShoppingCart, models.Q(recipe__id=pk))

    @action(
        methods=("GET",),
        detail=False,
        permission_classes=(IsAuthenticated,),
    )
    def download_shopping_cart(self, request: Request) -> Response:
        """
        Generate csv file and send Response with list of ingredients with total
        amount.
        """
        cart = ShoppingCart.objects.filter(user=request.user)
        recipes = [
            recipe.get("recipe_id")
            for recipe in cart.values()
            if recipe.get("recipe_id")
        ]
        ingredients = (
            IngredientRecipe.objects.filter(recipe_id__in=recipes)
            .values("ingredient_id__name", "ingredient_id__measurement_unit")
            .annotate(models.Sum("amount"))
        )
        result = list()
        for ingredient in ingredients:
            result.append(
                {
                    "Ингредиент": ingredient["ingredient_id__name"],
                    "Мера": ingredient["ingredient_id__measurement_unit"],
                    "Количество": ingredient["amount__sum"],
                }
            )

        response = HttpResponse(content_type="text/csv", charset="utf-8")
        response["Content-Disposition"] = "attachment; filename=cart.csv"

        writer = csv.DictWriter(
            response,
            fieldnames=["Ингредиент", "Мера", "Количество"],
            delimiter=";",
        )
        writer.writeheader()
        writer.writerows(result)
        return response
