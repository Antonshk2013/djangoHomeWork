from django.db import models
from src.task_manager.models.base import Status, BaseModel
from datetime import datetime


class Task(BaseModel):
    """Задача для выполнения."""
    title: str = models.CharField(
        max_length=255,
        unique_for_date='created_at',
    )
    categories = models.ManyToManyField('Category', related_name='tasks')


