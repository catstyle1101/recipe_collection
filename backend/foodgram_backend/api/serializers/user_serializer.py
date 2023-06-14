from django.db.models import Model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from users.models import Subscription, User


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
