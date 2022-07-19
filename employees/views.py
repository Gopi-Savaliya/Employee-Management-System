from datetime import datetime
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee, Department, Role


def index(request):
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees})


def add_employee(request):
    departments = Department.objects.all()
    roles = Role.objects.all()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department = Department.objects.get(name=request.POST.get('department', 'Developer'))
        department_id = department.id
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = Role.objects.get(name=request.POST.get('role', 'Jr. Software consultant'))
        role_id = role.id
        phone = int(request.POST['phone'])
        new_employee = Employee(first_name=first_name, last_name=last_name, department_id=department_id, salary=salary,
                                bonus=bonus, role_id=role_id, phone=phone, hire_date=datetime.now())
        new_employee.save()
        return render(request, 'add_employee.html',
                      {'msg': 'Employee Added Successfully', 'departments': departments, 'roles': roles})
    else:
        return render(request, 'add_employee.html', {'msg': '', 'departments': departments, 'roles': roles})


def remove_employee(request, emp_id=0):
    msg = ''
    if emp_id:
        try:
            delete_emp_id = Employee.objects.get(id=emp_id)
            delete_emp_id.delete()
            msg = 'Employee Deleted Successfully'
        except:
            return HttpResponse("Please enter valid Employee ID")
    employees = Employee.objects.all()
    return render(request, 'remove_employee.html', {'msg': msg, 'employees': employees})


def filter_employee(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    roles = Role.objects.all()
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        department = request.POST['department']
        role = request.POST['role']
        if name:
            employees = employees.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if department:
            employees = employees.filter(department__name=department)
        if role:
            employees = employees.filter(role__name=role)
        return render(request, 'filter_employee.html', {'employees': employees, 'departments': departments, 'roles': roles})
    else:
        return render(request, 'filter_employee.html', {'employees': employees, 'departments': departments, 'roles': roles})
