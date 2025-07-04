from django.urls import path
from django.http import HttpResponse
from src.new_app.views import hello_name


urlpatterns = [
    path('hello/<str:name>', hello_name, name='hello_name'),
]