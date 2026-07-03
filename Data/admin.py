from django.contrib import admin
from.models import Data,Department
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=['empid','empname','salary']
    list_editable=('salary',)

class DeptAdmin(admin.ModelAdmin):
    list_display=['deptid','deptname','location']
    list_editable=('location',)
admin.site.register(Data,EmpAdmin)
admin.site.register(Department,DeptAdmin)
