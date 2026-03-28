
from rest_framework import serializers
from departments.api.serializers import DepartmentSerializer
from departments.models import Department
from students.models import Student

# define serializers for models ?

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=200)
    age = serializers.IntegerField(default=10)
    gender = serializers.CharField(max_length=1)
    grade = serializers.CharField()
    image = serializers.ImageField(required=False)
    department_id = serializers.IntegerField()
    department = DepartmentSerializer(read_only=True)
    department_name = serializers.CharField(
        source='department',max_length=100, read_only=True)

    # add validation rules to serializers
    def validate_department_id(self, value):
        if Department.objects.filter(id=value).exists():
            return value
        else:
            raise serializers.ValidationError()
    # override create function
    def create(self, validated_data):
        student = Student.objects.create(**validated_data)
        return student

    # define update actions


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('id',)


