from django.db import models
from src.task_manager.models.base import Status, BaseModel
from datetime import datetime


class Task(BaseModel):
    """Задача для выполнения."""
    categories = models.ManyToManyField('Category', related_name='tasks')
    class Meta:
        db_table = 'task_manager_task'
        verbose_name = "Task"
        ordering = ['created_at']

    @property
    def short_description(self):
        return f"{self.description[:20]}..."

