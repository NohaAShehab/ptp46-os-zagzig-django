from django import forms

from departments.models import Department


class DepartmentModelForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'