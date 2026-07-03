from django.shortcuts import render

# Create your views here.
def eightfun(request):
    obj=render(request,'eight.html')
    return obj

