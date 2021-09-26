from project.models import *
from django.shortcuts import render
from django.core.paginator import Paginator


def get_data(request, department_id=1):
    department_name = Department.objects.get(id=department_id)
    department_employee = Employee.objects.filter(department_id=department_id).distinct()
    paginator = Paginator(department_employee, 50)  # Show 50 employes per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'department': Department.objects.all(),
        'department_name': department_name,
        'department_employee': department_employee,
        'page_obj': page_obj
    }
    return render(request, 'web_page.html', data)
