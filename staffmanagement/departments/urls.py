
from django.urls import path
from departments.views import landing as dept_landing, show as dept_show
urlpatterns = [
    path('landing', dept_landing, name='departments.landing'),
    path('<int:id>', dept_show, name='departments.show'),
]
