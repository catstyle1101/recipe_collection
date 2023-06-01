import re
from django.core.exceptions import ValidationError


def cooking_time_validator(number: int) -> None:
    if number < 1 or number > 32767:
        raise ValidationError(
            "Время готовки должно быть в диапазоне от 1 до 32767"
        )


def hex_validator(string: str) -> None:
    hex_pattern = r"^#[A-F0-9]{6}$"
    if not re.match(hex_pattern, string):
        raise ValidationError("Неверный формат HEX цвета")
