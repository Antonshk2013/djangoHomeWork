from django.urls import path
from src.task_manager.views import (
    SubTaskListCreateView,
    SubTaskDetailUpdateDeleteView,
)

urlpatterns = [
    path('', SubTaskListCreateView.as_view()),
    path('<int:subtask_id>/', SubTaskDetailUpdateDeleteView.as_view()),
]