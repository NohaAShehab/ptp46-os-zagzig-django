from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet


# get all students
from django.http import HttpResponse, JsonResponse
from students.models import Student
from students.api.serializers import StudentSerializer, StudentModelSerializer


# return with rest response

# def index(request):
#     students = Student.objects.all()
#     # serialization --> JSON,
#     serialized_objects  =[]
#     for student in students:
#         serialized_objects.append({
#             'id': student.id,
#             'name': student.name,
#         })
#
#     # return HttpResponse(students)
#     return  JsonResponse(serialized_objects, safe=False)

# you should tell me that this view is api view ??
# @api_view(['GET', 'POST'])
# def index(request):
#
#     if request.method == 'POST':
#         # read data from Post body
#         print(request.data)
#         # create new model object
#         # ** request.data ---> create(name='dsd', email='')
#         student = Student.objects.create(**request.data)
#         print(student.id)
#         # return with it ? so you need to serialize it first
#         student  = StudentSerializer(student)
#         return Response({'message': 'object created!',
#                          'student': student.data},status=status.HTTP_201_CREATED)
#     students = Student.objects.all()
#     # use serializer to prepare objects
#     students= StudentSerializer(students, many=True)
#
#     # return HttpResponse(students)
#     return  Response(students.data)


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        student  = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response({'message': 'object created!',
                         'student': student.data},status=status.HTTP_201_CREATED)
        return Response({'message': 'not valid',
                       'errors' :student.errors},status=status.HTTP_400_BAD_REQUEST)


    students = Student.objects.all()
    # use serializer to prepare objects
    students= StudentSerializer(students, many=True)

    # return HttpResponse(students)
    return  Response(students.data)

###########################################################

class StudentViewSet(ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()













