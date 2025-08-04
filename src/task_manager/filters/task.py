from django_filters import rest_framework as filters
from django.db.models.functions import ExtractWeekDay

from src.task_manager.models import Task, Status


class TaskFilter(filters.FilterSet):
    # WEEKDAYS = {
    #     'воскресенье': 1,
    #     'понедельник': 2,
    #     'вторник': 3,
    #     'среда': 4,
    #     'четверг': 5,
    #     'пятница': 6,
    #     'суббота': 7,
    # }

    # weekday = filters.ChoiceFilter(method='filter_by_weekday_name', choices=WEEKDAYS,)
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    status = filters.ChoiceFilter(choices=Status.choices())
    #
    # def filter_by_weekday_name(self, queryset, name, value):
    #     day_number = self.WEEKDAYS.get(value.strip().lower())
    #     if day_number is None:
    #         return queryset.none()
    #     return queryset.annotate(
    #         weekday=ExtractWeekDay('created_at')
    #     ).filter(weekday=day_number)

    class Meta:
        model = Task
        fields = [
            'title',
            'status',
        ]