from django.shortcuts import redirect

def checkinsertperm(fun):
    def innerfun(request):
        if request.user.has_perm('DBApp.insert_employee')==True:
            return fun(request)
        else:
            return redirect('selecturl',pno=1)
    return innerfun

def checkupdateperm(fun):
    def innerfun(request):
        if request.user.has_perm('DBApp.update_employee')==True:
            return fun(request)
        else:
            return redirect('selecturl',pno=1)
    return innerfun

def deleteperm(fun):
    def innerfun(request):
        if request.user.has_perm('DBApp.delete_employee')==True:
            return fun(request)
        else:
            return redirect('selecturl',pno=1)
    return innerfun