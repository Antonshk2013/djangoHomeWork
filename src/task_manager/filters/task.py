from django_filters import rest_framework as filters

from src.task_manager.models import Task, Status
from src.task_manager.filters.weekday_filter_mixin import WeekdayFilterMixin


class TaskFilter(filters.FilterSet, WeekdayFilterMixin):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')
    deadline = filters.DateFilter(field_name='deadline', lookup_expr='exact')
    status = filters.ChoiceFilter(choices=Status.choices())

    class Meta:
        model = Task
        fields = [
            'title',
            'status',
            'description',
            'deadline',
        ]