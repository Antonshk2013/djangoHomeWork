from django.urls import path
from src.task_manager.views import (
    get_task_report,
    TaskListApiView,
    TaskDetailApiView)

urlpatterns = [
    path('', TaskListApiView.as_view()),
    path('<int:task_id>/', TaskDetailApiView.as_view()),
    path('report/', get_task_report)
]