# Generated by Django 4.2.1 on 2023-06-01 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("foodgram", "0006_ingredient"),
    ]

    operations = [
        migrations.CreateModel(
            name="IngredientRecipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.IntegerField(verbose_name="Количество")),
                (
                    "ingredient_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="foodgram.ingredient",
                    ),
                ),
                (
                    "recipe_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="foodgram.recipe",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="recipe",
            name="ingredients",
            field=models.ManyToManyField(
                through="foodgram.IngredientRecipe", to="foodgram.ingredient"
            ),
        ),
    ]