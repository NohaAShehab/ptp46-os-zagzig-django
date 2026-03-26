from django.shortcuts import render, get_object_or_404
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