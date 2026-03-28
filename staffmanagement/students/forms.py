from random import choices

from django import forms

from departments.models import Department
from students.models import Student


class StudentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    grade = forms.IntegerField()
    image = forms.ImageField()
    gender = forms.ChoiceField(
        choices= [('m','Male' ),('f','Female')]
    )
    age= forms.IntegerField()
    department = forms.ModelChoiceField(queryset=Department.objects.all())

    # add validation rules ?
    def clean_email(self):
        # check if email exists --> display
        email = self.cleaned_data['email']
        found = Student.objects.filter(email=email).exists()
        if found:
            raise forms.ValidationError("Student with this email already exists")
        return email

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 0:
            raise forms.ValidationError("Student name is too short")
        return name


    def clean_grade(self):
        grade = self.cleaned_data['grade']
        if grade < 0 or grade > 100:
            raise forms.ValidationError("Grade must be between 0 and 100")
        return grade


    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 15 or age > 30:
            raise forms.ValidationError("Age must be between 15 and 30")
        return age

    # clean image --> allowed extensions



class StudentModelForm(forms.ModelForm):
    msg = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Student
        fields = '__all__'

    def clean_email(self):
        # check if email exists --> display
        email = self.cleaned_data['email']
        found = Student.objects.filter(email=email)
        if self.instance.pk :
            # if this form used with update action
            found = found.exclude(pk=self.instance.pk)
        if found.exists():
            raise forms.ValidationError("Student with this email already exists")
        return email

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 0:
            raise forms.ValidationError("Student name is too short")
        return name

    def clean_grade(self):
        grade = self.cleaned_data['grade']
        if grade < 0 or grade > 100:
            raise forms.ValidationError("Grade must be between 0 and 100")
        return grade

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 15 or age > 30:
            raise forms.ValidationError("Age must be between 15 and 30")
        return age