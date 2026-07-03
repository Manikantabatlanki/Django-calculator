from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Employee,Department
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from .decorators import checkinsertperm,checkupdateperm,deleteperm
# Create your views here.
def dbprocessing(request):
    return HttpResponse('DB request has been succesfully accepted')
@checkinsertperm
def insertemployee(request):
    if request.method=='GET':
        depts=Department.objects.all()
        return render(request,'DBApp/insert.html',{'department':depts})
    if request.method=='POST':
        eno=int(request.POST['eno'])
        ename=request.POST['ename']
        esal=int(request.POST['esal'])
        epic=request.FILES.get('epic')
        eobj=Employee.objects.create(empno=eno,empname=ename,salary=esal,profile_pic=epic)
        return redirect('selecturl',pno=1) 

@login_required(login_url='loginurl')
def selectemployee(request,pno):
    if request.method == 'GET':
        emps=Employee.objects.all()
        paginator_obj=Paginator(emps,1)
        page_obj=paginator_obj.get_page(pno)
        return render(request,'DBApp/select.html',{'employees':page_obj})
@checkupdateperm
def updateemployee(request,eno):
    if request.method == 'GET':
        eobj=Employee.objects.get(empno=eno)
        return render(request,'DBApp/update.html',{'employee':eobj})
    if request.method == 'POST':
        eno=int(request.POST['eno'])
        ename=request.POST['ename']
        esal=int(request.POST['esal'])
        epic=request.FILES.get('epic')
        eobj=Employee(empno=eno,empname=ename,salary=esal,profile_pic=epic)
        eobj.save()
        messages.success(request,'Updated succesfully')
        return redirect('selecturl',pno=1)
 
@deleteperm 
def deleteemployee(request,eno):
    if request.method == 'GET':
        eobj=Employee.objects.get(empno=eno)
        return render(request,'DBApp/delete.html',{'employe':eobj})
        return redirect('selecturl',pno=1)
    
    if request.method == 'POST':
        eobj=Employee.objects.get(empno=eno)
        eobj.delete()
        return redirect('selecturl',pno=1)


def detailemployee(request,eno):
    if request.method=='GET':
        request.session.modified=True
        emp=Employee.objects.get(empno=eno)
        if 'prev_emps' in request.session:
            request.session['prev_emps'].append(eno)
        else:
            request.session['prev_emps']=[eno]
        print(request.session['prev_emps'])
        prev_emp=Employee.objects.filter(Q(empno__in=request.session['prev_emps']) & ~Q(empno=eno))
        return render(request,'DBApp/detail.html',{'employee':emp,'previous':prev_emp})
    
def loginpage(request):
    if request.method=='GET':
        return render(request,'DBApp/login.html')
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
        emptyform=UserCreationForm()
        return render(request,'DBApp/register.html',{'form':emptyform})
    if request.method=='POST':
        dataform=UserCreationForm(request.POST)
        if dataform.is_valid()==True:
            dataform.save()
            return redirect('loginurl')
        else:
            return render(request,'DBApp/register.html',{'form':dataform})
        

        


  

    









