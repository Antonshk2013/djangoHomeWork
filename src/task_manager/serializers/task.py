from rest_framework import serializers

from src.task_manager.models import Task
from src.task_manager.serializers.subtusk import SubTaskCreateSerializer
from src.common.validators import validate_deadline_field



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
    subtasks = SubTaskCreateSerializer(many=True, read_only=True)
    deadline = serializers.DateTimeField(format="%d.%m.%Y")
    created_at = serializers.DateTimeField(format="%d.%m.%Y")
    class Meta:
        model = Task
        fields = ('__all__')
        read_only_fields = ('created_at')


class TaskCreateSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(
        format="%d.%m.%Y",
        validators=[
            validate_deadline_field
        ]
    )
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Task
        fields = ('__all__')
        exclude = ('created_at', 'updated_at')


