from datetime import datetime
from enum import Enum
from django.db import models


class Status(str, Enum):
    NEW = "New"
    IN_PROGRESS = "In progress"
    PENDING = "Pending"
    BLOCKED = "Blocked"
    DONE = "Done"

    @classmethod
    def choices(cls):
        return [(i.value, i.value) for i in cls]


class BaseModel(models.Model):
    title: str = models.CharField(
        max_length=255,
        unique=True,
    )
    description: str = models.TextField()
    status: str = models.CharField(
        max_length=255,
        choices=Status.choices()
    )
    deadline: datetime = models.DateTimeField()
    created_at: datetime = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.title} {self.status}'

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id}, title={self.title})'


