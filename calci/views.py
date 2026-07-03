from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def calcifun(request):
   if request.method=='GET':
      return render(request,'calci/calci.html')
   if request.method=='POST':
      v1=int(request.POST.get('t1'))
      v2=int(request.POST.get('t2'))
      if 'add' in request.POST:
         res=v1+v2
      elif 'sub' in request.POST:
         res=v2-v1
      elif 'multi' in request.POST:
         res=v1*v2
      else:
         res=v1/v2
      return render(request,'calci/calci.html',{'result':res})

