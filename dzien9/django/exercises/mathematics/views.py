from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse(f"Hello in mathematics applications")

def add_variable(request,variable1,variable2):
    var1 = int(variable1)
    var2 = int(variable2)
    var3 = int(var1 + var2)
    return HttpResponse(f"Suma {var3}")

def roznica_variable(request,var1,var2):
    variable1 = int(var1)
    variable2 = int(var2)
    variable3 = int(variable1 - variable2)
    return HttpResponse(f"Różnica {variable3}")