from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from Data.models import Data
from django.urls import reverse_lazy
from django.views.generic import ListView
# Create your views here.


class Calculator(View):
    def get(self,request):
        return render(request,'classApp/Addition.html')
    def post(self,request):
        v1=int(request.POST['t1'])
        v2=int(request.POST['t2'])
        res=v1+v2
        return render(request,'classApp/Addition.html',{'result':res})


class Calculator2(Calculator):
    def post(self,request):
        v1=int(request.POST['t1'])
        v2=int(request.POST['t2'])
        res=v1*v2
        return render(request,'classApp/multi.html',{'result':res})

class InsertView(CreateView):
    model=Data
    fields='__all__'
    template_name='classApp/insertview.html'
    success_url=reverse_lazy('selecturl',kwargs={'pno':1})

class ModifyView(UpdateView):
    model=Data
    fields='__all__'
    template_name='classApp/updateview.html'
    success_url=reverse_lazy('selecturl',kwargs={'pno':1})


class SelectView(ListView):
    model=Data
    fields='__all__'
    template_name='classApp/selectview.html'

class DeleteView(DeleteView):
    model=Data
    fields='__all__'
    template_name='classApp/Deleteview.html'
    success_url=reverse_lazy('selecturl',kwargs={'pno':1})
    


