from django_filters import rest_framework as filters
from django.db.models.functions import ExtractWeekDay


class WeekdayFilterMixin:
    WEEKDAYS = {
        'воскресенье': 1,
        'понедельник': 2,
        'вторник': 3,
        'среда': 4,
        'четверг': 5,
        'пятница': 6,
        'суббота': 7,
    }

    weekday = filters.ChoiceFilter(method='filter_by_weekday_name', choices=WEEKDAYS, )

    def filter_by_weekday_name(self, queryset, name, value):
        day_number = self.WEEKDAYS.get(value.strip().lower())
        if day_number is None:
            return queryset.none()
        return queryset.annotate(
            weekday=ExtractWeekDay('created_at')
        ).filter(weekday=day_number)

