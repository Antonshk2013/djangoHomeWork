from django.db import models
from django.contrib.auth import get_user_model

from src.task_manager.models.base import Status, BaseModel


User = get_user_model()


class Task(BaseModel):
    """Задача для выполнения."""
    categories = models.ManyToManyField('Category', related_name='tasks')
    owner = models.ForeignKey(User,
                              null=True,
                              on_delete=models.CASCADE,
                              related_name='tasks')
    class Meta:
        db_table = 'task_manager_task'
        verbose_name = "Task"
        ordering = ['created_at']

    @property
    def short_description(self):
        return f"{self.description[:20]}..."

