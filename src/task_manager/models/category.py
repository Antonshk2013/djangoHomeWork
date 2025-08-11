from django.utils import timezone

from django.db import models


class ActiveCategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Category(models.Model):
    """Категория выполнения."""
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()
    soft_delete_objects = ActiveCategoryManager()

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name})"

    def delete(self, using=None, keep_parents=False):
        """Мягкое удаление: только пометка, без физического удаления."""
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super().delete()