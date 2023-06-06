from collections import defaultdict

from django.db import models
from django.db.transaction import atomic
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from foodgram.models import Recipe, IngredientRecipe, Tag, Ingredient
from users.serializers import CustomUserSerializer
from .tag_serializer import TagSerializer


class RecipeSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True, default=serializers.CurrentUserDefault())
    ingredients = serializers.SerializerMethodField()
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()
    image = Base64ImageField()
    tags = TagSerializer(many=True, read_only=True)

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
        read_only_fields = (
            "is_favorited",
            "is_in_shopping_cart",
        )

    @atomic
    def create(self, validated_data):
        tags = validated_data.pop("tags")
        ingredients = validated_data.pop("ingredients")
        recipe = Recipe.objects.create(**validated_data)
        recipe.tags.set(tags)
        IngredientRecipe.objects.bulk_create(
            [
                IngredientRecipe(
                    recipe_id=recipe,
                    ingredient_id=ingredient,
                    amount=amount,
                )
                for ingredient, amount in ingredients.values()
            ]
        )
        return recipe

    @atomic
    def update(self, recipe, validated_data):
        tags = validated_data.pop("tags")
        ingredients = validated_data.pop("ingredients")

        for key, value in validated_data.items():
            if hasattr(recipe):
                setattr(recipe, key, value)
        if tags:
            recipe.tags.clear()
            recipe.tags.set(tags)
        if ingredients:
            recipe.ingredients.clear()
            IngredientRecipe.objects.bulk_create(
                [
                    IngredientRecipe(
                        recipe_id=recipe,
                        ingredient_id=ingredient,
                        amount=amount,
                    )
                    for ingredient, amount in ingredients.values()
                ]
            )
        recipe.save()
        return recipe

    def get_ingredients(self, recipe):
        return recipe.ingredients.values(
            "id", "name", "measurement_unit", amount=models.F("ingredientrecipe__amount")
        )

    def get_is_favorited(self, recipe):
        user = self.context.get("view").request.user
        if user.is_anonymous:
            return False
        return user.favorites.filter(recipe=recipe).exists()

    def get_is_in_shopping_cart(self, recipe):
        user = self.context.get("view").request.user
        if user.is_anonymous:
            return False
        return user.cart.filter(recipe=recipe).exists()

    def validate(self, attrs):
        tags = self.initial_data.get("tags")
        ingredients = self.initial_data.get("ingredients")
        if not tags or not ingredients:
            raise ValidationError("Не все поля заполнены")
        if len(tags) != len(Tag.objects.filter(id__in=tags)):
            raise ValidationError("Указан неверный тег")
        valid_ingredients = defaultdict(int)
        for ingredient in ingredients:
            if (
                not str(ingredient["amount"]).isdigit()
                or int(ingredient["amount"]) < 1
            ):
                raise ValidationError("Введено неверное количество")
            valid_ingredients[int(ingredient["id"])] += int(
                ingredient["amount"]
            )
        if not valid_ingredients:
            raise ValidationError("Не указаны ингредиенты")
        database_ingredients = Ingredient.objects.filter(
            pk__in=valid_ingredients.keys()
        )
        if not database_ingredients:
            raise ValidationError("Нет ингредиентов в базе")
        data = dict()
        for ingredient in database_ingredients:
            data[ingredient.pk] = (
                ingredient,
                valid_ingredients[ingredient.pk],
            )

        attrs.update(
            {
                "tags": tags,
                "ingredients": data,
                "author": self.context.get("request").user,
            }
        )
        return attrs
