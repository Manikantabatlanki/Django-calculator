from django.db import models

# Create your models here.
class Department(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptname=models.CharField(max_length=20)
    location=models.CharField(max_length=30)
    def __str__(self):
        return self.deptname
class Employee(models.Model):
    empno = models.AutoField(primary_key=True)
    empname = models.CharField(max_length=20)
    salary = models.IntegerField(null=True)
    dept = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    profile_pic=models.ImageField(upload_to="images/",null=True,blank=True)

    def __str__(self):
        return self.empname


