
from django.urls import path
from departments.views import (landing as dept_landing, show as dept_show
, create, DepartmentCreateView)
urlpatterns = [
    path('landing', dept_landing, name='departments.landing'),
    path('<int:id>', dept_show, name='departments.show'),
    # path('create', create, name='create'),
    path('create', DepartmentCreateView.as_view(), name='departments.create'),
]
