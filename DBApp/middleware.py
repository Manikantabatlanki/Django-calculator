


class CustomMiddleWare:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print('before reaching view')
        resp=self.get_response(request)
        print('after reacing view')
        return resp