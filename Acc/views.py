from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Accfun(request):
    if request.method=='GET':
        return render(request,'Acc/Acc.html')
    if request.method=='POST':
        return render(request,'Acc/Acc.html')
    
def Acc2fun(request):
    if request.method=='GET':
        return render(request,'Acc2/Acc2.html')
    

