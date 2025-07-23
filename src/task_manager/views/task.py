from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from src.task_manager.services import TaskService
from src.common.services import ErrorType

@api_view(['POST', 'GET'])
def get_all_tasks(request: Request) -> Response:
    if request.method == 'GET':
        service = TaskService()
        result = service.get_all_tasks()
        if result.success:
            return Response(
                data=result.data,
                status=status.HTTP_200_OK
            )
        return Response(
            data=result.message,
            status=status.HTTP_400_BAD_REQUEST
        )
    if request.method == 'POST':
        service = TaskService()
        result = service.create_new_task(request.data)
        if result.success:
            return Response(
                data=result.data,
                status=status.HTTP_201_CREATED
            )
        else:
            if result.error_type == ErrorType.VALIDATION_ERROR.value:
                return Response(
                    data=result.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                return Response(
                    data=result.errors,
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )


@api_view(['GET'])
def get_task(request: Request, task_id: int) -> Response:
    service = TaskService()
    result = service.get_task(
        task_id
    )
    if result.success:
        return Response(
            data=result.data,
            status=status.HTTP_200_OK
        )
    return Response(
        data=result.errors,
        status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET'])
def get_task_report(request: Request) -> Response:
    service = TaskService()
    result = service.get_task_report()
    if result.success:
        return Response(
            data=result.data,
            status=status.HTTP_200_OK
        )
    return Response(
        data=result.errors,
        status=status.HTTP_400_BAD_REQUEST
        )



