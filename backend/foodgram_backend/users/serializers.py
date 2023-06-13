from django.conf import settings
from django.db.models import Model
from djoser.serializers import UserSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import Subscription
from users.models import User
from foodgram.models import Recipe


class ShortRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ("id", "name", "image", "cooking_time")
        read_only_fields = ("id", "name", "image", "cooking_time")



class CustomUserSerializer(UserSerializer):
    """
    User serializer. Checks if user is subscribed to another user.
    """
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "email",
            "id",
            "username",
            "first_name",
            "last_name",
            "is_subscribed",
        )

    def get_is_subscribed(self, obj: Model) -> bool:
        """
        Check if user is subscribed to another user.
        """
        user_id = self.context.get("request").user.id
        return Subscription.objects.filter(
            user_id=user_id, author_id=obj.id
        ).exists()


class UserSubscribeSerializer(CustomUserSerializer):
    """
    Serialiser for subscribed users page.
    """
    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.SerializerMethodField()
    is_subscribed = serializers.BooleanField(read_only=True, default=True)

    class Meta:
        model = User
        fields = (
            "email",
            "id",
            "username",
            "first_name",
            "last_name",
            "recipes",
            "is_subscribed",
            "recipes_count",
        )
        read_only_fields = (
            "email",
            "id",
            "username",
            "first_name",
            "last_name",
            "recipes",
            "is_subscribed",
            "recipes_count",
        )

    def get_recipes_count(self, obj: Model) -> int:
        """
        Counts of all recipes of user.
        """
        return obj.recipes.count()

    def get_recipes(self, obj: Model) -> Recipe:
        """
        Get 3 recipes.
        """
        recipes = obj.recipes.all()[:settings.MAX_RECIPES_IN_SUB_PAGE]
        serializer = ShortRecipeSerializer(recipes, many=True, read_only=True)
        return serializer.data

    def validate(self, attrs):
        if attrs.get("user") == attrs.get("author"):
            raise ValidationError("Нельзя подписаться на самого себя")
        if Subscription.objects.get(
                user=attrs.get("user"), author=attrs.get("author")).exists():
            raise ValidationError("Нельзя подписаться дважды")
        return attrs
