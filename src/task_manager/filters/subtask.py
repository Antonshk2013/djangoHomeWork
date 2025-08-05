from django_filters import rest_framework as filters

from src.task_manager.models import Status
from src.task_manager.models.subtask import SubTask

class SubTaskFilter(filters.FilterSet):

    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    status = filters.ChoiceFilter(choices=Status.choices())
    task_name = filters.CharFilter(
        field_name='task__title',
        lookup_expr='icontains')

    class Meta:
        model = SubTask
        fields = [
            'title',
            'status',
            'task_name',
        ]
