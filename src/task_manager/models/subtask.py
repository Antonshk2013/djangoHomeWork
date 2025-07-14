from django.db import models
from src.task_manager.models.base import Status, BaseModel
from datetime import datetime


class SubTask(BaseModel):
    """Отдельная часть основной задачи (Task)"""
    task: int = models.ForeignKey(
        'Task',
        on_delete=models.CASCADE,
        related_name='subtasks'
    )

    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ['created_at']
        verbose_name = 'SubTask'

    @property
    def short_title(self):
        return f"{self.title[:10]}..."