
from django.urls import path
from students.views import  (
    home, hi, profile,student_profile, landing, index, create ,
    delete, create_via_form, CreateStudent, UpdateStudent)
# you define name for each url , you can use this name, in views, models, in template pages ..
urlpatterns = [
    path('home', home, name='home'),
    path('abbass', hi, name='hi'),
    # username is param read from the url
    path('user/<username>', profile, name='profile'),
    path('<int:id>', student_profile, name='students.profile'),
    path('land', landing, name='landing'),
    path('index', index, name='students.index'),
    path('create', create, name='students.create'),
    path('delete/<int:id>', delete, name='students.delete'),
    path('create_via_form', create_via_form, name='students.create_via_form'),
    path('generic', CreateStudent.as_view(), name='students.generic.create'),
    path('update/<int:pk>', UpdateStudent.as_view(), name='students.update'),
]
