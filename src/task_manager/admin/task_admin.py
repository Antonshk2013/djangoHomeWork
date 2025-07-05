from django.contrib import admin
from src.task_manager.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'deadline', 'created_at')
    search_fields = ['title', 'description']



admin.site.register(Task, TaskAdmin)