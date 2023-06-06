from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint, CheckConstraint, Q


class User(AbstractUser):
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
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_user(self):
        return self.role == 'user'


class Subscription(models.Model):
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
            CheckConstraint(
                check=~models.Q(user=models.F("author")),
                name="Нельзя подписаться на самого себя",
            ),
        )
