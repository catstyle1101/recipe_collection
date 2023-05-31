from django.db import models
from django.conf import settings

# from users.models.users import User
from .validators import cooking_time_validator


class Recipe(models.Model):
    name = models.CharField(
        "Название",
        max_length=settings.MAX_RECIPE_NAME_LENGTH,
    )
    image = models.ImageField("Картинка")
    text = models.TextField("Описание")
    cooking_time = models.PositiveSmallIntegerField(
        "Время приготовления (в минутах)", validators=(cooking_time_validator,)
    )
    # author = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name="recipe_author",
    #     verbose_name="Автор рецепта",
    # )
    # tags = models.ManyToManyField(
    #     "Tag",
    # )
