from django.contrib import admin
from.models import Employee,Department
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=('empno','empname','salary')
class DeptAdmin(admin.ModelAdmin):
    list_display=('deptno','deptname','location')
    list_editable=('location',)
admin.site.register(Employee,EmpAdmin)
admin.site.register(Department,DeptAdmin)