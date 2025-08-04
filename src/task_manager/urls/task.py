from django.urls import path
from src.task_manager.views import (
    # get_all_tasks,
    # get_task,
    # get_task_report,
    TaskListApiView)

urlpatterns = [
    path('', TaskListApiView.as_view()),
    # path('', get_all_tasks),
    # path('<int:task_id>/', get_task),
    # path('report/', get_task_report)
]