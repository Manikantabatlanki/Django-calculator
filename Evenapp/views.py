from django.shortcuts import render

# Create your views here.
def evenfun(request):
    if request.method=='GET':
        obj=render(request,'even.html')
        return obj
    if request.method=='POST':
        t1=int(request.POST.get('t1'))

        if t1 %2 ==0:
            result=f'{t1} is even'
        else:
            result=f'{t1} is odd'
        return render(request,'even.html',{'result':result})
