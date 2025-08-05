from django.urls import path, include

urlpatterns = [
    path('tasks/', include('src.task_manager.urls.task')),
    path('subtasks/', include('src.task_manager.urls.subtask')),
    path('category/', include('src.task_manager.urls.category')),
]