from django import forms
from .models import Student, Representative, Course, Teacher, Inscription, Payment

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
        fields = ['name', 'teacher']
        widgets = {
            'teacher': forms.CheckboxSelectMultiple(),
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

