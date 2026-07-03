from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def addition(request):
    if request.method == 'GET':
        return render(request,'Calculator/addition.html')
    if request.method == 'POST':
        #print(request.POST)
        v1=int(request.POST.get('t1'))
        v2=int(request.POST.get('t2'))
        res=v1+v2
        return render(request,'calculator/addition.html',{'output':res})
    
def mathtable(request):
    if request.method == 'GET':
        return render(request,'Calculator/mtable.html')
    
    if request.method == 'POST':
        output=[]
        n=int(request.POST.get('t1'))
        for i in range(1,11):
            output.append(str(n) + '*'+ str(i)+' = ' +str(i*n))
        return render(request,'Calculator/mtable.html',{'output':output})