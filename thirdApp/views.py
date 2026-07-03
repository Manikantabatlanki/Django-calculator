from django.shortcuts import render
from django .http import HttpResponse
# Create your views here.
def thirdfun(request):
   obj=render(request,'third.html')
   return obj

