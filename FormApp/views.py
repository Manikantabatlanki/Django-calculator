from django.shortcuts import render
from django.http import HttpResponse
from.forms import FirstForm,EmpForm
# Create your views here.
def firstform(request):
    if request.method=='GET':
        emptyform=FirstForm()
        return render(request,'FormApp/first.html',{'form':emptyform})

    if request.method=='POST':
        emptyform=EmpForm()
        dataform=FirstForm(request.POST)
        if dataform.is_valid()==True:
            v1=dataform.cleaned_data['value1']
            v2=dataform.cleaned_data['value2']
            res=v1+v2
            return render(request,'formApp/first.html',{'result':res,'form':emptyform})
        else:
            return render(request,'formApp/first.html',{'form':dataform})
        
def insertemployee(request):
        if request.method=='GET':
            emptyform=EmpForm()
            return render(request,'formApp/insert.html',{'form':emptyform})
        
        if request.method=='POST':
             print(request.FILES)
             emptyform=EmpForm()
             dataform=EmpForm(request.POST,request.FILES)
             if dataform.is_valid():
                  dataform.save()
                  return render(request,'formApp/insert.html',{'form':emptyform})
                  


