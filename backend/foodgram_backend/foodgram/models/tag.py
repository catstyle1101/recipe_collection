from django.conf import settings
from django.db import models

from .validators import hex_validator


class Tag(models.Model):
    name = models.CharField(
        "Название",
        max_length=settings.MAX_TAG_NAME_LENGTH,
    )
    color = models.CharField(
        "Цвет",
        max_length=7,
        help_text="Цвет в HEX. Пример: #000000",
        validators=(hex_validator,),
    )
    slug = models.SlugField(
        unique=True,
    )

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name
