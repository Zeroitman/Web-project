from django.conf.urls import url
from project.views import *

urlpatterns = [
    url(r'department/(?P<department_id>\d+)', get_data, name="index"),
    url(r'^$', get_data, name="index"),
]
