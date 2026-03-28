
from rest_framework import serializers
from departments.api.serializers import DepartmentSerializer
from departments.models import Department
from students.models import Student

# define serializers for models ?

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=200)
    age = serializers.IntegerField(default=10)
    gender = serializers.CharField(max_length=1)
    grade = serializers.CharField()
    image = serializers.ImageField()
    department_id = serializers.IntegerField()
    department = DepartmentSerializer(read_only=True)
    department_name = serializers.CharField(
        source='department',max_length=100)


    # override create function
    def create(self, validated_data):
        student = Student.objects.create(**validated_data)
        return student
