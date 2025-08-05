from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from src.task_manager.models import Category, Task
from src.task_manager.serializers import CategorySerializer
from src.task_manager.services.category import CategoryService


class CategoryViewSet(ModelViewSet):
    queryset = Category.soft_delete_objects.all()
    serializer_class = CategorySerializer


    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        count_tasks = Task.objects.filter(categories=pk).count()
        return Response({'count_tasks': count_tasks})

