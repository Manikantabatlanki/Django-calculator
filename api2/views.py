from django.shortcuts import render
from Data.models import Data
from .serializer import EmpSerializer,CustomSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND
from rest_framework .views import APIView
from rest_framework.pagination import PageNumberPagination
# Create your views here.

@api_view(['GET','POST'])
def getemployees(request):
    if request.method=='GET':
        emps=Data.objects.all()
        s_obj=EmpSerializer(emps,many=True)
        return Response(s_obj.data)
    if request.method=='POST':
        s_obj=EmpSerializer(data=request.data)
        if s_obj.is_valid()==True:
            s_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)
        
@api_view(['PUT','GET','DELETE'])  
def updateapi(request,eno):
    if request.method=='GET':
        emps=Data.objects.get(empid=eno)
        s_obj=EmpSerializer(emps)
        return Response(s_obj.data,status=HTTP_200_OK)
    if request.method=='PUT':
        emps=Data.objects.get(empid=eno)
        s_obj=EmpSerializer(emps,data=request.data)
        if s_obj.is_valid()==True:
            s_obj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        emp=Data.objects.get(empid=eno)
        emp.delete()
        return Response(status=HTTP_200_OK)
    
@api_view(['GET','POST'])
def CustomApi(request):
    if request.method=='GET':
        return Response(status=HTTP_200_OK)
    if request.method=='POST':
        s_obj=CustomSerializer(data=request.data)
        if s_obj.is_valid()==True:
            eobj=s_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)



class EmployeApiView(APIView):
    def get(self,request):
        emp=Data.objects.all()
        paginator=PageNumberPagination()
        paginator.page_size=2
        p_queryset=paginator.paginate_queryset(emp,request)

        s_obj=EmpSerializer(p_queryset,many=True)
        return paginator.get_paginated_response(s_obj.data)

