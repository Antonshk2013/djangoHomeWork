from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_name(request, name: str) -> HttpResponse:
    return HttpResponse(f"Hello {name.capitalize()}!")
