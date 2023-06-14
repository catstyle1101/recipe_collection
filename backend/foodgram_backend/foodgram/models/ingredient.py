from django.conf import settings
from django.db import models

from foodgram.models.validators import ingredient_validator


class Ingredient(models.Model):
    """
    Ingredient model. Fields:
    - name (Charfield)
    - measurement unit (Charfield)
    """
    name = models.CharField(
        "Название ингредиента",
        max_length=settings.MAX_INGREDIENT_NAME_LENGTH,
    )
    measurement_unit = models.CharField(
        "Единицы измерения",
        max_length=settings.MAX_INGREDIENT_UNIT_NAME_LENGTH,
    )

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"
        ordering = ("name",)

    def __str__(self):
        return (
            f"{self.name[:settings.MAX_ADMIN_MODEL_NAME_LENGTH]}: "
            f"{self.measurement_unit[:settings.MAX_ADMIN_MODEL_NAME_LENGTH]}"
        )


class IngredientRecipe(models.Model):
    """
    Model for bind Ingredient with Recipe models. Add amount of ingredient
    for a recipe.
    Fields:
    - recipe_id (FK Recipe)
    - ingredient_id (FK Ingredient)
    - amount (IntegerField)
    """
    recipe_id = models.ForeignKey(
        "Recipe",
        on_delete=models.CASCADE,
    )
    ingredient_id = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
    )
    amount = models.PositiveSmallIntegerField(
        "Количество",
        validators=(ingredient_validator,)
    )
