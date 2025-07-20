from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, DatabaseError

from src.task_manager.repositories import TaskRepository
from src.task_manager.serializers import (
    TaskListSerializer,
    TaskSerializer,
    TaskDetailSerializer,)
from src.common.services import ServiceResponse, ErrorType

class TaskService:
    def __init__(self):
        self.repository = TaskRepository()

    def get_all_tasks(self)-> ServiceResponse:
        try:
            tasks = self.repository.get_all()
            serializer = TaskListSerializer(
                tasks,
                many=True)
            return ServiceResponse(
                success=True,
                data=serializer.data
            )
        except Exception as e:
            return ServiceResponse(
                success=False,
                error_type=ErrorType.UNKNOWN_ERROR.value,
                message=str(e)
            )

    def create_new_task(self, task_dict: dict) -> ServiceResponse:
        serializer = TaskSerializer(data=task_dict)
        if not serializer.is_valid():
            return ServiceResponse(
                success=False,
                error_type=ErrorType.VALIDATION_ERROR.value,
                errors=serializer.errors
            )
        try:
            task=self.repository.create(**serializer.validated_data)
            return ServiceResponse(
                success=True,
                data=task.to_dict()
            )
        except IntegrityError as e:
            return ServiceResponse(success=False, error_type=ErrorType.INTEGRITY_ERROR, message=str(e))
        except DatabaseError as e:
            return ServiceResponse(success=False, error_type=ErrorType.UNKNOWN_ERROR, message=str(e))

    def get_task(self, task_id: str) -> ServiceResponse:
        try:
            task = self.repository.get_by_id(id_=task_id)
            serializer = TaskDetailSerializer(task)
            return ServiceResponse(
                success=True,
                data=serializer.data
            )
        except ObjectDoesNotExist as e:
            return ServiceResponse(
                success=False,
                error_type=ErrorType.NOT_FOUND.value,
                errors=str(e)
            )
        except IntegrityError as e:
            return ServiceResponse(
                success=False,
                error_type=ErrorType.INTEGRITY_ERROR.value,
                errors=str(e)
            )
        except DatabaseError as e:
            return ServiceResponse(
                success=False,
                error_type=ErrorType.UNKNOWN_ERROR.value,
                errors=str(e)
            )

    def get_task_report(self)-> ServiceResponse:
        try:
            report = self.repository.get_task_report()
            return ServiceResponse(
                success=True,
                data=report
            )
        except Exception as e:
            return ServiceResponse(
                success=False,
                error_type=ErrorType.UNKNOWN_ERROR.value,
                message=str(e)
            )






