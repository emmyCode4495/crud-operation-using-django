from django import forms
from .models import Employee

class Employee_Form(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','mobile','emp_code','position')
        labels = {
            'fullname': 'Full Name',
            'mobile': 'Mobile Number',
            'emp_code': 'EMP. Code',

        }

    def __init__(self, *args, **kwargs):
        super(Employee_Form, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
  