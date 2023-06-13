from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint
from rest_framework.exceptions import ValidationError


class User(AbstractUser):
    """
    Usermodel. login field is email, requered fields:
    - email
    - first_name
    - last_name
    - username
    """
    USER = "user"
    ADMIN = "admin"
    ROLE_CHOICES = (
        (USER, "Авторизованный пользователь"),
        (ADMIN, "Администратор"),
    )
    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default=USER,
        verbose_name="Роль",
    )
    email = models.EmailField(
        "Адрес электронной почты",
        unique=True,
    )
    username = models.CharField(
        "Имя пользователя",
        max_length=settings.MAX_USERNAME_LENGTH,
    )
    first_name = models.CharField(
        "Имя",
        max_length=settings.MAX_FIRSTNAME_LENGTH,
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=settings.MAX_LASTNAME_LENGTH,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username", "first_name", "last_name")

    @property
    def is_admin(self) -> bool:
        """
        Checks if user is admin role.
        """
        return self.role == self.ADMIN or self.is_superuser or self.is_staff

    @property
    def is_user(self) -> bool:
        """
        Checks if user is user role.
        """
        return self.role == self.USER

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


class Subscription(models.Model):
    """
    M2M related model for user subscriptions. Fields:
    - author (FK User)
    - user (FK user)
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscribers"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = (
            UniqueConstraint(
                fields=("user", "author"),
                name="Нельзя подписаться дважды",
            ),
        )

    def clean(self):
        if self.user == self.author:
            raise ValidationError("Нельзя подписаться на самого себя")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
