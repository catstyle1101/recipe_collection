# Generated by Django 4.2.1 on 2023-06-01 07:27

import foodgram.models.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Recipe",
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
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="Название"),
                ),
                (
                    "image",
                    models.ImageField(upload_to="", verbose_name="Картинка"),
                ),
                ("text", models.TextField(verbose_name="Описание")),
                (
                    "more_than_one_validator",
                    models.PositiveSmallIntegerField(
                        validators=[
                            foodgram.models.validators.more_than_one_validator
                        ],
                        verbose_name="Время приготовления (в минутах)",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рецепт",
                "verbose_name_plural": "Рецепты",
            },
        ),
        migrations.CreateModel(
            name="Subscription",
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
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="Название"),
                ),
                (
                    "color",
                    models.CharField(
                        help_text="Цвет в HEX",
                        max_length=7,
                        validators=[foodgram.models.validators.hex_validator],
                        verbose_name="Цвет",
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
            ],
        ),
    ]
