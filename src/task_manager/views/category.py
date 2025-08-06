from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import (
    IsAuthenticated,
    DjangoModelPermissions
)


from src.task_manager.models import Category, Task
from src.task_manager.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.soft_delete_objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        count_tasks = Task.objects.filter(categories=pk).count()
        return Response({'count_tasks': count_tasks})

