from django.urls import path, include

urlpatterns = [
    path('tasks/', include('src.task_manager.urls')),
]