from django.db import models
from src.task_manager.models.base import Status, BaseModel
from datetime import datetime


class SubTask(BaseModel):
    """Отдельная часть основной задачи (Task)"""
    task: int = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='subtasks')