from django.shortcuts import render
from django.http import HttpResponse
# Create your views he
def colorfun(request):
    if request.method=='GET':
        return render(request,'color/color.html')
    if request.method=='POST':
        v1=int(request.post.get('t1').value)
        v2=int(request.post.get('t2').value)
        res=v1*v2
        return render(request,'color/color.html',{'result':res})
