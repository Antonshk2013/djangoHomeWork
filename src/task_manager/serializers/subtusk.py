from rest_framework import serializers

from src.task_manager.models import SubTask
from src.task_manager.repositories import SubTaskRepository
from src.common.validators import validate_deadline_field

class SubTaskCreateSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(
        format="%d.%m.%Y",
        validators=[
            validate_deadline_field
        ]
    )
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