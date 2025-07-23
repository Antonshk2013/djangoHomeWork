from django.db import DatabaseError, OperationalError
from django.db.models import Count, Case, When, Value, IntegerField, Sum
from django.utils.timezone import now

from src.common.repositories import BaseRepository
from src.task_manager.models.subtask import SubTask


class SubTaskRepository(BaseRepository):
    def __init__(self):
        super().__init__(SubTask)