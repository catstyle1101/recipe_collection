from django.db import models
from rest_framework.exceptions import ValidationError

from users.models import User


class Subscription(models.Model):
    author_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_id'
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_id',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("author_id", "user_id"),
                name="unique_subscription",
            ),
        ]

    def clean(self):
        if self.author_id == self.user_id:
            raise ValidationError('Нельзя подписаться на самого себя!')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
