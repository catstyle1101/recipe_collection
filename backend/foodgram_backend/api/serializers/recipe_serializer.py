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
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = (
            "id",
            "tags",
            "author",
            "ingredients",
            # "is_favorited",
            # "is_in_shopping_cart",
            "name",
            "image",
            "text",
            "cooking_time",
        )

    def create(self, validated_data):
        return Recipe.objects.create(**validated_data)
