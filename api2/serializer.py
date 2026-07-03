from rest_framework import serializers
from Data.models import Data
from DBApp.models import Employee
from rest_framework .response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from rest_framework.exceptions import ValidationError
class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields='__all__'

class CustomSerializer(serializers.Serializer):
    eno=serializers.IntegerField()
    ename=serializers.CharField(max_length=20)
    esal=serializers.IntegerField()
    bonus=serializers.IntegerField()

    def validated_esal(self,sal):
        if sal<0:
            raise ValidationError('Negative salary is not accepeted')
        return sal
    
    def create(self,validated_data):
        eobj=Data.objects.create(empid=validated_data['eno'],\
                            empname=validated_data['ename'],\
                            salary=validated_data['esal']+validated_data['bonus'])
        return eobj
            


