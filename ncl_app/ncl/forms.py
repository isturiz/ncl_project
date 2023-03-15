from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'birthdate', 'age_category', 'representative')
