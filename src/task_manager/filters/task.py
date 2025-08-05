from django_filters import rest_framework as filters

from src.task_manager.models import Task, Status
from src.task_manager.filters.weekday_filter_mixin import WeekdayFilterMixin


class TaskFilter(filters.FilterSet, WeekdayFilterMixin):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    status = filters.ChoiceFilter(choices=Status.choices())

    class Meta:
        model = Task
        fields = [
            'title',
            'status',
        ]