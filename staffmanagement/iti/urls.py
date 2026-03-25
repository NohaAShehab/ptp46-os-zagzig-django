"""
URL configuration for iti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
# from students.views import  home, hi, profile, student_profile, landing
from departments.views import landing as dept_landing
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home', home, name='home'),
    # path('abbass', hi, name='hi'),
    # # username is param read from the url
    # path('user/<username>', profile, name='profile'),
    # path('student/<int:id>', student_profile, name='student_profile'),
    # path('land', landing, name='landing'),

    # path('department/landing', dept_landing, name='departments.landing'),
    path('students/', include('students.urls')),
    path('departments/', include('departments.urls'))

]
