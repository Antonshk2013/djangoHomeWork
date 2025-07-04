from django.urls import path, include

urlpatterns = [
    path('new_app/', include('src.new_app.urls')),
]