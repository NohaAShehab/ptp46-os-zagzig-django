from django.shortcuts import render, get_object_or_404, redirect
from django.views import  View
from departments.forms import DepartmentModelForm
from departments.models import Department


# Create your views here.


def landing(request):
    departments = Department.objects.all()
    return render(request, 'departments/landing.html',
                  context={'departments': departments})


def show(request, id ):
    department = get_object_or_404(Department, id=id)
    return render(
        request,
        'departments/show.html',
        context={'department': department},
    )


def create(request):
    form = DepartmentModelForm()
    if request.method == "POST":
        form = DepartmentModelForm(request.POST, request.FILES)
        if form.is_valid():
            department = form.save()
            return redirect("departments.show", id=department.id)

    return render(request, "departments/create.html", context={"form": form})




### class based views

class DepartmentCreateView(View):
    def get(self, request):
        form  = DepartmentModelForm()
        return render(request, "departments/create.html", context={"form": form})

    def post(self, request):
        form = DepartmentModelForm(request.POST, request.FILES)
        if form.is_valid():
            department = form.save()
            return redirect("departments.show", id=department.id)
        return render(request, "departments/create.html", context={"form": form})













