
from students.api.views import  index, StudentViewSet
from django.urls import path , include

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'stds', StudentViewSet, basename='stds')

# create routes for student
"""
    get /students/ --> all students
    post /students/ --> create new student
    get /students/id --> get student
    put /students/id --> update student
    delete /students/id --> delete student

"""
urlpatterns = [
    path('index', index, name='students.api.index'),
    path('gen/', include(router.urls)),
]