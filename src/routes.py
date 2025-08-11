from django.urls import path, include

urlpatterns = [
    path('', include('src.task_manager.urls')),
    path('custom_auth/', include('src.users.urls')),

]