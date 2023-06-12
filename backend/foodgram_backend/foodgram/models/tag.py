from django.conf import settings
from django.db import models
from colorfield.fields import ColorField


class Tag(models.Model):
    """
    Tag model. Fields:
    - name (CharField)
    - color (CharField)
    - slug (SlugField)
    """
    name = models.CharField(
        "Имя тега",
        max_length=settings.MAX_TAG_NAME_LENGTH,
        unique=True,
    )
    color = ColorField(
        "Цвет",
        format="hex",
        unique=True,
    )
    slug = models.SlugField(
        unique=True,
    )

    def clean(self):
        self.name = self.name.lower()
        self.color = self.color.upper()
        self.slug = self.slug.lower()
        return super().clean()

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name[:settings.MAX_ADMIN_MODEL_NAME_LENGTH]
