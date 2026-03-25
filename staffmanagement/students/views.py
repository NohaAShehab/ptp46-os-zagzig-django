from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# create my first view handle http request
# function view ?

def home(request): # this function will handle http request ?
    print("---- Hello request ----")
    print(request)
    # I need to return with http response
    return HttpResponse("Hello World")



def hi(request):
    return HttpResponse("<h1 style='color:red'> Hi User</h1>")


def profile(request, username):
    print(username)
    return HttpResponse(f"<h1 style='color:red'> Hi User: {username}</h1>")


students = [
    {"id":1, "name":"Ali", "track": "os", "salary": 1000},
    {"id": 2, "name": "Test", "track": "os", "salary": 5000},
    {"id":3, "name":"Abc", "track": "os", "salary": 4000},
]


def student_profile(request, id):
    print(id, type(id))
    student_found = filter(lambda student: student["id"] == int(id), students)
    student_found = list(student_found)
    if len(student_found) == 0:
        return HttpResponse("<h1 style='color:red'> No user found</h1>")

    student = student_found[0]
    return HttpResponse(f"<h1 style='color:red'> Hi {student['id']} {student['name']}</h1>")


