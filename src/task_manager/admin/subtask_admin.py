from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse

from src.task_manager.models import Status
from src.task_manager.models import SubTask


@admin.register(SubTask)
class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_short_title', 'status', 'task', 'deadline', 'created_at')
    search_fields = ['title', 'description']
    actions = ['mark_done']

    @admin.display(description='Short Title')
    def display_short_title(self, obj):
        return str(obj.short_title)

    @admin.action(description="Set Done status ")
    def mark_done(self, request: HttpRequest, subtasks: QuerySet):
        subtasks.update(status=Status.DONE.value)
        return request



