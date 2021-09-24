from django.views.generic import ListView
from project.models import Employee


class EmployeeListView(ListView):
    model = Employee
    template_name = 'web_page.html'

    def get_queryset(self):
        return Employee.objects.all()
