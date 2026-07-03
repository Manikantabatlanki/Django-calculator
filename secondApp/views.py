from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def secondfun(request):
    obj=render(request,'second.html')
    return obj