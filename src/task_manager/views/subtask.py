from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from src.task_manager.services import SubTaskService
from src.task_manager.serializers import SubTaskCreateSerializer
from src.task_manager.filters import SubTaskFilter


class SubTaskListApiView(ListCreateAPIView):
    service = SubTaskService()
    queryset = service.repository.get_all()
    serializer_class = SubTaskCreateSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = SubTaskFilter
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['title']


class SubTaskDetailApiView(RetrieveUpdateDestroyAPIView):
    service = SubTaskService()
    queryset = service.repository.get_all()
    serializer_class = SubTaskCreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'subtask_id'