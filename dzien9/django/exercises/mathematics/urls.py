from django.urls import path
from mathematics.views import hello, add_variable, roznica_variable


urlpatterns = [
    path('', hello),
    path('add/<variable1>/<variable2>', add_variable),
    path('roznica/<var1>/<var2>', roznica_variable),
]