from django.shortcuts import render

# Create your views here.
def sevenfun(request):
    obj=render(request,'seven.html')
    return obj
