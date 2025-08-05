from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.decorators import api_view
from rest_framework import status

from src.task_manager.filters import TaskFilter
from src.task_manager.services import TaskService
from src.task_manager.serializers import TaskSerializer


class TaskListApiView(ListCreateAPIView):
    service = TaskService()
    queryset = service.repository.get_all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    ordering = ['title']


class TaskDetailApiView(RetrieveUpdateDestroyAPIView):
    service = TaskService()
    queryset = service.repository.get_all()
    serializer_class = TaskSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'task_id'


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



