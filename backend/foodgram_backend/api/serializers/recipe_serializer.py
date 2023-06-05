from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from foodgram.models import Recipe
from users.serializers import CustomUserSerializer
from .ingredient_serializer import IngredientRecipeSerializer


class RecipeSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()
    ingredients = IngredientRecipeSerializer(
        source='ingredientrecipe_set',
        many=True,
        read_only=True,
    )
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = (
            "id",
            "tags",
            "author",
            "ingredients",
            "is_favorited",
            "is_in_shopping_cart",
            "name",
            "image",
            "text",
            "cooking_time",
        )

    def create(self, validated_data):
        return Recipe.objects.create(**validated_data)

    def get_is_favorited(self, recipe):
        user = self.context.get('view').request.user
        if user.is_anonymous:
            return False
        return user.favorites.filter(recipe=recipe).exists()

    def get_is_in_shopping_cart(self, recipe):
        user = self.context.get('view').request.user
        if user.is_anonymous:
            return False
        return user.cart.filter(recipe=recipe).exists()



