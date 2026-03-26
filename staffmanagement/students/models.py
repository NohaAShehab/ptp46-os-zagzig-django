from django.db import models
from django.shortcuts import reverse
# Create your models here.


"""
    name,  (varchar)
    email,  (varchar)
    grade, (int)
    image, (varchar)
    gender, (varchar , enum)
    age  (int)
    
    models.model => import provide datatypes --> 
    match needed datatypes in mysql 
"""
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, null=True, unique=True )  # validate email , backend
    grade = models.IntegerField(default=0)
    image=  models.CharField(max_length=200, null=True)
    gender = models.CharField(choices=[('m','Male'), ('f','Female')],
                              max_length=1, default='m')
    age = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        # represent how object will be printed , return with string ?
        return f'{self.name}'

    @property
    def image_url(self):
        return f'students/images/{self.image}'


    @property
    def show_url(self):
        return reverse("students.profile", args=[self.id])
