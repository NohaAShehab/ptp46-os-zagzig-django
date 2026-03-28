from rest_framework import serializers


class DepartmentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    logo = serializers.ImageField()
    about = serializers.CharField(required=False)