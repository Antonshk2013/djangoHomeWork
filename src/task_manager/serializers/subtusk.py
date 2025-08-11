from typing import Any

from rest_framework import serializers

from src.task_manager.models import SubTask
from src.task_manager.repositories import SubTaskRepository
from src.common.validators import validate_deadline_field

class SubTaskCreateSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(
        format="%d.%m.%Y",
        input_formats=["%d.%m.%Y"],
        validators=[
            validate_deadline_field
        ]
    )
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SubTask
        fields = '__all__'
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        repository = SubTaskRepository()
        try:
            subtask = repository.create(**validated_data)
            return subtask
        except Exception as e:
            raise serializers.ValidationError(str(e))

    def update(self, instance: SubTask, validated_data: dict[str, Any]) -> SubTask:
        repository = SubTaskRepository()
        try:
            updated_subtask = repository.update(instance.id, **validated_data)
            return updated_subtask
        except Exception as e:
            raise serializers.ValidationError(str(e))