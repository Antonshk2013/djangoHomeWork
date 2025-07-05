from django.db import models


class Category(models.Model):
    """Категория выполнения."""
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name})"