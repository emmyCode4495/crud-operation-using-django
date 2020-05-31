from django.shortcuts import render,redirect
from .forms import Employee_Form
from .models import Employee

def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request,"register/employee_list.html",context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = Employee_Form()
        else:
            employee = Employee.objects.get(pk=id)
            form = Employee_Form(instance=employee)
        return render(request,"register/employee_form.html",{"form":form})
    else:
        if id==0:
            form = Employee_Form(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = Employee_Form(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
    