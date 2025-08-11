from django.db import models
from django.contrib.auth import get_user_model

from src.task_manager.models.base import Status, BaseModel

User = get_user_model()

class SubTask(BaseModel):
    """Отдельная часть основной задачи (Task)"""
    task: int = models.ForeignKey(
        'Task',
        on_delete=models.CASCADE,
        related_name='subtasks'
    )
    owner = models.ForeignKey(User,
                              null=True,
                              on_delete=models.CASCADE,
                              related_name='sub_tasks')

    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ['created_at']
        verbose_name = 'SubTask'

    @property
    def short_title(self):
        return f"{self.title[:10]}..."