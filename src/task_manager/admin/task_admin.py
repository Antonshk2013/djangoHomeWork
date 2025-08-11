from django.contrib import admin

from src.task_manager.models import Task, SubTask


class SubtaskInline(admin.TabularInline):
    model = SubTask
    extra = 1
    min_num = 1
    max_num = 25
    fields = [
        "title",
        "description",
        "status",
        "deadline"
    ]
    readonly_fields = [
        "created_at"
    ]
    verbose_name = "Subtask under this task."
    verbose_name_plural = "Subtasks under this task."

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [SubtaskInline]

    list_display = ('id', 'title', 'status', 'deadline', 'created_at')
    search_fields = ['title', 'description']

