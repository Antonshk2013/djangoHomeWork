from django.db import models


class Category(models.Model):
    """Категория выполнения."""
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name})"