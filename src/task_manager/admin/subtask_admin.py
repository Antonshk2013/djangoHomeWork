from django.contrib import admin
from src.task_manager.models import SubTask

class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'task', 'deadline', 'created_at')
    search_fields = ['title', 'description']



admin.site.register(SubTask, SubtaskAdmin)