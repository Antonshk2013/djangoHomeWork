from django.urls import path


from src.task_manager.views import (
    SubTaskListApiView,
    SubTaskDetailApiView,
)

urlpatterns = [
    path('', SubTaskListApiView.as_view()),
    path('<int:subtask_id>/', SubTaskDetailApiView.as_view()),
]