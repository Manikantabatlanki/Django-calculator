from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Rufffun(request):
    return render(request,'Ruff/Ruff.html')
