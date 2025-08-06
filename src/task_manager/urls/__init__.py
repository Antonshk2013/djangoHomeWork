from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('tasks/', include('src.task_manager.urls.task')),
    path('subtasks/', include('src.task_manager.urls.subtask')),
    path('category/', include('src.task_manager.urls.category')),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]