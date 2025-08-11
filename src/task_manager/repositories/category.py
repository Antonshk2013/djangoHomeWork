from typing import TypeVar, Optional
from django.db.models import Model
from django.db import DatabaseError, OperationalError

from src.common.repositories import BaseRepository
from src.task_manager.models.category import Category


Model_ = TypeVar('Model_', bound=Model)


class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Category)

    def get_by_name(self, name: str) -> Optional[Model_]:
        if name:
            try:
                category = self.model.objects.get(name__lower=name.lower())
                return category
            except self.model.DoesNotExist:
                return None
            except DatabaseError as e:
                raise OperationalError(f'Failed to retrieve {self.model.__name__} with id {name}') from e
        else:
            raise ValueError('Name must be non-empty string')