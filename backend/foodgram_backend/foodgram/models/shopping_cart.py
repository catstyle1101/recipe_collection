from django.db import models
from django.db.models import UniqueConstraint

from users.models import User
from . import Recipe


class ShoppingCart(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        related_name="in_cart",
        verbose_name="Рецепты в корзине",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        related_name="cart",
        verbose_name="Ваша корзина",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Корзина покупателя"
        verbose_name_plural = "Корзины покупателей"
        constraints = (
            UniqueConstraint(
                fields=("user", "recipe"),
                name="Рецепт уже в корзине",
            ),
        )
