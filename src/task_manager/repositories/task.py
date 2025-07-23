from django.db import DatabaseError, OperationalError
from django.db.models import Count, Case, When, Value, IntegerField, Sum
from django.utils.timezone import now

from src.common.repositories import BaseRepository
from src.task_manager.models.task import Task


class TaskRepository(BaseRepository):
    def __init__(self):
        super().__init__(Task)

    def get_task_report(self):
        try:
            today = now().date()
            report = self.model.objects.annotate(
                is_overdue=Case(
                    When(deadline__date__lt=today, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField()
                )
            ).values('status').annotate(
                count_tasks=Count('id'),
                count_overdue=Sum('is_overdue')
            )
            return report
        except DatabaseError as e:
            raise OperationalError(f'Failed to retrieve {self.model.__name__} objects') from e

