from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated,
    DjangoModelPermissions
)

from src.task_manager.filters import TaskFilter
from src.task_manager.services import TaskService
from src.task_manager.serializers import TaskSerializer
from src.task_manager.permissions import IsOwner


class TaskListApiView(ListCreateAPIView):
    service = TaskService()
    queryset = service.repository.get_all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TaskFilter
    search_fields = [
        'title',
        'description',
    ]
    ordering_fields = ['created_at']
    ordering = ['title']
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class TaskDetailApiView(RetrieveUpdateDestroyAPIView):
    service = TaskService()
    queryset = service.repository.get_all()
    serializer_class = TaskSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'task_id'
    permission_classes = [IsAuthenticated, DjangoModelPermissions, IsOwner]



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



