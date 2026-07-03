from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def subfun(request):
    if request.method=='GET':
        return render(request,'sub.html')
    if request.method=='POST':
        t1=int(request.POST.get('t1'))
        t2=int(request.POST.get('t2'))
        res=t2-t1
        return render(request,'sub.html',{'res':res})