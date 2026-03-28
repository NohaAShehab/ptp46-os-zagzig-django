
from students.api.views import  index
from django.urls import path
urlpatterns = [
    path('index', index, name='students.api.index')
]