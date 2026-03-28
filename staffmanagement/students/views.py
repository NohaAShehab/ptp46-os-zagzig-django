from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from departments.models import Department
from students.models import Student
from students.forms import StudentForm

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

#
# def student_profile(request, id):
#     print(id, type(id))
#     student_found = filter(lambda student: student["id"] == int(id), students)
#     student_found = list(student_found)
#     if len(student_found) == 0:
#         return HttpResponse("<h1 style='color:red'> No user found</h1>")
#
#     student = student_found[0]
#     return HttpResponse(f"<h1 style='color:red'> Hi {student['id']} {student['name']}</h1>")


# return content in html page ??


def landing(request):
    # return ...  return with page --> landing.html ??
    return render(request, "students/landing.html")

#
# def index(request):
#     # send information of all students to the index.html
#     return render(request, "students/index.html",
#                   context={'name': "noha",
#                            "students": students})



# def student_profile(request, id):
#     student_found = filter(lambda student: student["id"] == id, students)
#     student_found = list(student_found)
#     if len(student_found) == 0:
#         return HttpResponse("<h1 style='color:red'> No user found</h1>")
#
#     student = student_found[0]
#     return render(request, "students/profile.html",
#                   context={"student": student})




def index(request):
    students = Student.objects.all()
    # send information of all students to the index.html
    return render(request, "students/index.html",
                  context={'name': "noha",
                           "students": students})


def student_profile(request, id):
    # student= Student.objects.get(id=id)
    # student = Student.objects.filter(id=id).first()
    # if not student:
    #     return HttpResponse("Student not found")
    student= get_object_or_404(Student, pk=id)
    return render(request, "students/profile.html",
                  context={"student": student})


def create(request):
    departments = Department.objects.all()
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        age = request.POST.get("age", "").strip()
        grade = request.POST.get("grade", "").strip()
        gender = request.POST.get("gender", "m").strip() or "m"

        # If image input is type="file", Django provides it via request.FILES.
        image = request.FILES.get("image")
        # image = image_file.name if image_file else request.POST.get("image", "").strip()

        department = request.POST.get("department")  ## this is the id of the dept ??
        ## in django department must a model object -->
        department = Department.objects.filter(pk=department).first()
        # errors = {}
        # if len(name) <2  or  image==None or int(age) > 100:
        #     errors["name"]="name must be > 2  characters"
        #     errors["age"]="age must be < 100 characters"
        #     errors ["image"] = "Image is required"
        # if errors:
        #     return render(request, "students/create.html", context={"errors": errors})

        student = Student(
            name=name,
            email=email,
            age=int(age) if age else 10,
            grade=int(grade) if grade else 0,
            image=image or None,
            gender=gender if gender in {"m", "f"} else "m",
            department = department or None
        )
        student.save()
        return redirect(student.show_url)

    return render(request, "students/create.html",
                  context={"departments": departments})


def delete(request, id):
    student= get_object_or_404(Student, pk=id)
    student.delete() # delete from students_student where id = id;
    return redirect('students.index')



def create_via_form(request):
    form  = StudentForm()
    if request.method == "POST":
        print(request.POST)
        # I need to use the form to validate input
        form  = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            # prepare data storage, trim whitespaces,
            # string  --> casted to int --> convert empty values to None,
            print(form.cleaned_data)
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email", "")
            age = form.cleaned_data.get("age", "")
            grade = form.cleaned_data.get("grade", "")
            gender = form.cleaned_data.get("gender", "m").strip() or "m"
            image = form.cleaned_data.get("image")
            department = form.cleaned_data.get("department")
            # department = Department.objects.filter(pk=department).first()

            student = Student(
                name=name,
                email=email,
                age=int(age) if age else 10,
                grade=int(grade) if grade else 0,
                image=image or None,
                gender=gender if gender in {"m", "f"} else "m",
                department=department or None
            )
            student.save()
            return redirect(student.show_url)

    return render(request, "students/create_via_form.html", {"form": form})
