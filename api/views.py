from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from DBApp.models import Employee
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import EmpSerializer
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND
# Create your views here.
@api_view(['GET','POST'])
def getemployees(request):
    if request.method=='GET':
        emps=Employee.objects.all()
        s_obj=EmpSerializer(emps,many=True)
        return Response(s_obj.data,status=HTTP_200_OK)
    if request.method=='POST':
        s_obj=EmpSerializer(data=request.data)
        if s_obj.is_valid():
            s_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)
    
@api_view(['PUT','GET'])    
def update(request,eno):
    if request.method=='GET':
        emp=Employee.objects.get(empno=eno)
        s_obj=EmpSerializer(emp)
        return Response(s_obj.data,status=HTTP_200_OK)
    if request.method=='PUT':
        emp=Employee.objects.get(empno=eno)
        s_obj=EmpSerializer(emp,data=request.data)
        if s_obj.is_valid()==True:
            s_obj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
def delete(request, eno):
    if request.method=='DELETE':
        emp = Employee.objects.get(empno=eno)
        emp.delete()
        return Response({"message": "Employee deleted successfully"}, status=HTTP_200_OK)
    else:
         return Response({"message": "Employee not found"}, status=HTTP_404_NOT_FOUND)
        