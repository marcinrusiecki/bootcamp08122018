from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse(f"Hello world")

def hello_name(request,name):
    return HttpResponse(f"Hello {name}")

# Create your views here.
