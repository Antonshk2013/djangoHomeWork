from django_filters import rest_framework as filters

from src.task_manager.models import Status
from src.task_manager.models.subtask import SubTask

class SubTaskFilter(filters.FilterSet):

    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')
    status = filters.ChoiceFilter(choices=Status.choices())
    deadline = filters.DateFilter(field_name='deadline', lookup_expr='exact')
    task_name = filters.CharFilter(
        field_name='task__title',
        lookup_expr='icontains')

    class Meta:
        model = SubTask
        fields = [
            'title',
            'status',
            'task_name',
            'description',
            'deadline',
        ]
