from django import forms
from .models import Student, Representative, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class RepresentativeForm(forms.ModelForm):
    class Meta:
        model = Representative
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
