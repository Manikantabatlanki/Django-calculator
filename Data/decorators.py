from django.shortcuts import redirect
def chkinsertperm(fun):
    def innerfun(request):
        if request.user.has_perm('Data.insert_data')==True:
            return fun(request)
        else:
            return redirect('selecturl',pno=1)
    return innerfun

def chkupdateperm(fun):
    def innerfun(request,eid):
        if request.user.has_perm('Data.change_data')==True:
            return fun(request,eid)
        else:
            return redirect('selecturl',pno=1)
    return innerfun

