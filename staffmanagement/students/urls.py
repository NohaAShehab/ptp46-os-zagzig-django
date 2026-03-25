
from django.urls import path
from students.views import  home, hi, profile, student_profile, landing
urlpatterns = [
    path('home', home, name='home'),
    path('abbass', hi, name='hi'),
    # username is param read from the url
    path('user/<username>', profile, name='profile'),
    path('student/<int:id>', student_profile, name='student_profile'),
    path('land', landing, name='landing'),
]
