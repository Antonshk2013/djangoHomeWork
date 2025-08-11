from rest_framework.viewsets import ModelViewSet

from src.task_manager.repositories import CategoryRepository


class CategoryService:
    def __init__(self):
        self.repository = CategoryRepository()