from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Data,Department
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,permission_required
from .forms import Userform
from django.contrib.auth.forms import UserCreationForm
from .decorators import chkinsertperm,chkupdateperm
# Create your views here.
def dataprocess(request):
    return HttpResponse('DAta app is success')

@chkinsertperm
def insertemployee(request):
    if request.method=='GET':
        depts=Department.objects.all()
        return render(request,'Data/insert.html',{'department':depts})
    if request.method=='POST':
        eid=int(request.POST['eid'])
        ename=request.POST['ename']
        esal=int(request.POST['esal'])
        dno=int(request.POST['dept'])
        dobj=Department.objects.get(deptid=dno)
        eobj=Data.objects.create(empid=eid,empname=ename,salary=esal,dept=dobj)
        return redirect('selecturl',pno=1)
    
@permission_required('Data.view_data',login_url='loginurl')   
@login_required(login_url='loginurl')
def selectemployee(request,pno):
    if request.method=='GET':
        emps=Data.objects.all()
        paginator_obj=Paginator(emps,1)
        page_obj=paginator_obj.get_page(pno)
        return render(request,'Data/select.html',{'employees':page_obj})
    
@chkupdateperm
def updateemployee(request,eid):
    if request.method=='GET':
        eobj=Data.objects.get(empid=eid)
        depts=Department.objects.all()
        return render(request,'Data/update.html',{'employee':eobj,'departments':depts})
    
    if request.method=='POST':
        eid=int(request.POST['eid'])
        ename=request.POST['ename'] 
        esal=int(request.POST['esal'])
        dno=int(request.POST['dept'])
        dobj=Department.objects.get(deptid=dno)
        eobj=Data(empid=eid,empname=ename,salary=esal,dept=dobj)
        eobj.save()
        messages.success(request,'Updated succesfully')
        return redirect('selecturl',pno=1)
    
def deleteemployee(request,eid):
    if request.method=='GET':
        eobj=Data.objects.get(empid=eid)
        return render(request,'Data/delete.html',{'employee':eobj})
    if request.method=='POST':
        eobj=Data.objects.get(empid=eid)
        eobj.delete()
        return redirect('selecturl',pno=1)
    
def loginpage(request):
    if request.method=='GET':
        return render(request,'Data/login.html')
    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        valid_user=authenticate(request,username=uname,password=pwd)
        if valid_user is None:
            return redirect('loginurl')
        else:
            login(request,valid_user)
            return redirect('selecturl',pno=1)
        
def logoutpage(request):
    logout(request)
    return redirect('loginurl')

def registerpage(request):
    if request.method=='GET':
        emptyform=Userform()
        return render(request,'Data/register.html',{'form':emptyform})
    if request.method=='POST':
        dataform=Userform(request.POST)
        if dataform.is_valid()==True:
            dataform.save()
            return redirect('loginurl')
        else:
            return render(request,'Data/register.html',{'form':dataform})
        
    


    
    





