from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, DatabaseError

from src.task_manager.repositories import SubTaskRepository
from src.task_manager.serializers import (
    SubTaskCreateSerializer
)
from src.common.services import ServiceResponse, ErrorType


class SubTaskService:
    def __init__(self):
        self.repository = SubTaskRepository()

    def get_all_subtasks(self) -> ServiceResponse:
        try:
            subtasks = self.repository.get_all()
            serializer = SubTaskCreateSerializer(subtasks, many=True)
            return ServiceResponse(
                success=True,
                data=serializer.data)
        except Exception as e:
            return ServiceResponse(
                success=False,
                error_type=ErrorType.UNKNOWN_ERROR,
                message=str(e)
            )

    def create(self, subtask_dict: dict) -> ServiceResponse:
        serializer = SubTaskCreateSerializer(data=subtask_dict)
        if not serializer.is_valid():
            return ServiceResponse(
                success=False,
                error_type=ErrorType.VALIDATION_ERROR,
                errors=serializer.errors
            )
        try:
            subtask = serializer.save()
            return ServiceResponse(
                success=True,
                data=serializer.data
            )
        except Exception as e:
            return ServiceResponse(
                success=False,
                error_type=ErrorType.VALIDATION_ERROR,
                errors=serializer.errors
            )
