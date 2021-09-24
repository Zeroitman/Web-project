from django.urls import path
from project.views import EmployeeListView

urlpatterns = [
    path('web', EmployeeListView.as_view(), name='post_list'),
]
