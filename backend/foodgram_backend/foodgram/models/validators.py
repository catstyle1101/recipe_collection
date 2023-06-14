from django.conf import settings
from django.core.exceptions import ValidationError


def postitve_not_nul_max_validator(number: int) -> None:
    """
    Check number is bigger than one and lesser than max
    SmallIntegerField value.
    """
    if number < 1 or number > settings.MAX_VALUE_IN_INT_FIELD:
        raise ValidationError(
            f"Время готовки должно быть в диапазоне "
            f"от 1 до {settings.MAX_VALUE_IN_INT_FIELD }"
        )


def ingredient_validator(number: int) -> None:
    """
    Check number is bigger than one and lesser than max
    SmallIntegerField value.
    """
    if number < 1 or number > settings.MAX_VALUE_IN_INT_FIELD:
        raise ValidationError(
            f"Количество ингредиента должно быть в диапазоне "
            f"от 1 до {settings.MAX_VALUE_IN_INT_FIELD }"
        )
