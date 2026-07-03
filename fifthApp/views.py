from django.shortcuts import render

# Create your views here.
def fifthfun(request):
    obj=render(request,'fifth.html')
    return obj