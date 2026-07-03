from django import forms
from django.core.exceptions import ValidationError
from DBApp.models import Employee
class FirstForm(forms.Form):
    value1=forms.IntegerField()
    value2=forms.IntegerField()
    dob=forms.DateField(widget=forms.SelectDateWidget)

    def clean_value1(self):
        v1=self.cleaned_data['value1']
        if v1<0:
            raise ValidationError('Negative values are not allowed')
        return v1
    
class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
