from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Addition(request):
    if request.method=='GET':
        return render(request,'calculator2/addition.html')
    if request.method=='POST':
        print(request.POST)
        v1=int(request.POST.get('t1'))
        v2=int(request.POST.get('t2'))
        if 'add' in request.POST:
            res=v1+v2
        elif 'sub' in request.POST:
            res=v1-v2
        elif 'multi' in request.POST:
            res=v1*v2
        else:
            res=v1/v2
        return render(request,'calculator2/addition.html',{'result':res})