from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, DatabaseError

from src.task_manager.models import SubTask
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

    def get_one_by_id(self, subtask_id: str) -> ServiceResponse:
        try:
            subtask = self.repository.get_by_id(id_=subtask_id)
            if subtask is None:
                return ServiceResponse(
                    success=False,
                    error_type=ErrorType.NOT_FOUND,
                    message='Subtask does not exist'
                )
            serializer = SubTaskCreateSerializer(subtask)
            return ServiceResponse(
                success=True,
                data=serializer.data
            )
        except ServiceResponse as e:
            return ServiceResponse(
                success=False,
                message=f"Can`t extract subtask {subtask_id}"
                )

    def update(self, subtask_id: int, subtask_data: dict, partial: bool = False) -> ServiceResponse:
        try:
            subtask = self.repository.get_by_id(id_=subtask_id)
            if not subtask:
                return ServiceResponse(
                    success=False,
                    error_type=ErrorType.NOT_FOUND,
                )
            serializer = SubTaskCreateSerializer(
                instance=subtask,
                data=subtask_data,
                partial=partial
            )
            if not serializer.is_valid():
                return ServiceResponse(
                    success=False,
                    error_type=ErrorType.VALIDATION_ERROR,
                    errors=serializer.errors
                )
            serializer.save()
            return ServiceResponse(
                success=True,
                data=serializer.data
            )
        except Exception as e:
            return ServiceResponse(
                success=False,
                error_type=ErrorType.UNKNOWN_ERROR,
                message=str(e)
            )
    def delete(self, subtask_id: str) -> ServiceResponse:
        subtask = self.repository.get_by_id(subtask_id)
        if not subtask:
            return ServiceResponse(
                success=False,
                error_type=ErrorType.NOT_FOUND,
            )
        subtask.delete()
        return ServiceResponse(
            success=True
        )

