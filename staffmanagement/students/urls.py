
from django.urls import path
from students.views import  (
    home, hi, profile,student_profile, landing, index, create)
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
]
