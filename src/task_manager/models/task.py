from django.db import models
from src.task_manager.models.base import Status, BaseModel
from datetime import datetime


class Task(BaseModel):
    """Задача для выполнения."""
    categories = models.ManyToManyField('Category', related_name='tasks')


