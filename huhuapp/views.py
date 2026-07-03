from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def huhufun(request):
    obj=render(request,'huhuapp/huhu.html')
    return obj
