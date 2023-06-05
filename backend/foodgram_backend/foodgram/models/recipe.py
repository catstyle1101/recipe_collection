from django.db import models
from django.conf import settings
from django.db.models import UniqueConstraint
from PIL import Image

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
        "Ingredient", through=IngredientRecipe, related_name="ingredients"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipe_author",
        verbose_name="Автор рецепта",
    )
    tags = models.ManyToManyField(
        "Tag",
        related_name='tags',
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ("-pub_date",)

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        image = image.resize(settings.RECIPE_IMAGE_SIZE)
        image.save(self.image.path)

    def __str__(self):
        return self.name


class FavoriteRecipe(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        verbose_name="Рецепты в избранном",
        related_name="in_favorites",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        related_name="favorites",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Избранный рецепт'
        verbose_name_plural = 'Избранные рецепты'
        constraints = (
            UniqueConstraint(
                fields=("recipe", "user"),
                name="Добавить рецепт в избранное можно только один раз",
            ),
        )
