from project.models import *
from django.shortcuts import render


def get_data(request, department_id=1):
    department_name = Department.objects.get(id=department_id)
    department_employee = Employee.objects.filter(department_id=department_id).distinct()
    data = {
        'department': Department.objects.all(),
        'department_name': department_name,
        'department_employee': department_employee,
    }
    return render(request, 'web_page.html', data)
