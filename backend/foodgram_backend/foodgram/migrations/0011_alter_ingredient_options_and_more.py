# Generated by Django 4.2.1 on 2023-06-09 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import foodgram.models.validators


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "foodgram",
            "0010_favoriterecipe_alter_shoppingcart_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ingredient",
            options={
                "ordering": ("name",),
                "verbose_name": "Ингредиент",
                "verbose_name_plural": "Ингредиенты",
            },
        ),
        migrations.RenameField(
            model_name="recipe",
            old_name="more_than_one_validator",
            new_name="cooking_time",
        ),
        migrations.AlterField(
            model_name="ingredientrecipe",
            name="amount",
            field=models.PositiveSmallIntegerField(
                validators=[
                    foodgram.models.validators.more_than_one_validator
                ],
                verbose_name="Количество",
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Рецепты",
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="tags",
            field=models.ManyToManyField(
                related_name="tags", to="foodgram.tag"
            ),
        ),
        migrations.DeleteModel(
            name="Subscription",
        ),
    ]
