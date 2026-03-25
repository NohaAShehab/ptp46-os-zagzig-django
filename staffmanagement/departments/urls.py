
from django.urls import path
from departments.views import landing as dept_landing
urlpatterns = [
    path('landing', dept_landing, name='departments.landing'),
]
