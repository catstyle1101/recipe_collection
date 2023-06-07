from django.conf import settings
from django.db import models


class Ingredient(models.Model):
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
        return f"{self.name}: {self.measurement_unit}"


class IngredientRecipe(models.Model):
    recipe_id = models.ForeignKey(
        "Recipe",
        on_delete=models.CASCADE,
    )
    ingredient_id = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField(
        "Количество",
    )
