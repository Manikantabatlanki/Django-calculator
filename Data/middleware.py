
from django.shortcuts import redirect
class MyMiddleWare:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print('before reaching the  view')
        
        resp=self.get_response(request)
        print('after reacing  the view')
        return resp
