from rest_framework import serializers

from src.task_manager.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'status',
            'deadline'
    )

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'short_description',
            )

class TaskDetailSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(format="%d.%m.%Y")
    created_at = serializers.DateTimeField(format="%d.%m.%Y")
    class Meta:
        model = Task
        fields = ('__all__')

