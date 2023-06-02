from django.db import models
from django.conf import settings

from users.models import User
from . import IngredientRecipe
from .validators import cooking_time_validator


class Recipe(models.Model):
    name = models.CharField(
        "Название",
        max_length=settings.MAX_RECIPE_NAME_LENGTH,
    )
    image = models.ImageField(
        "Картинка",
    )
    text = models.TextField("Описание")
    cooking_time = models.PositiveSmallIntegerField(
        "Время приготовления (в минутах)", validators=(cooking_time_validator,)
    )
    ingredients = models.ManyToManyField(
        "Ingredient",
        through=IngredientRecipe,
        related_name='ingredients'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipe_author",
        verbose_name="Автор рецепта",
    )
    tags = models.ManyToManyField(
        "Tag",
    )

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.name
