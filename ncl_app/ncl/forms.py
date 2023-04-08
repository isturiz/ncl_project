from django import forms
from .models import Student, Representative, Course, Teacher, Inscription, Payment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class RepresentativeForm(forms.ModelForm):
    class Meta:
        model = Representative
        fields = [
            'first_name', 
            'last_name',
            'email',
            'phone_number',
        ]
        labels = {
            'first_name': 'Nombre', 
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'phone_number': 'Número de teléfono',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'validateLetters shadow-sm border text-sm rounded-lg block w-full p-2.5 bg-gray-600 border-gray-500 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500', 'placeholder': 'Nombre', 'pattern': '[A-Za-z]+', 'oninput': 'validarLetras("name")', 'maxlength': '50', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'validateLetters shadow-sm border text-sm rounded-lg block w-full p-2.5 bg-gray-600 border-gray-500 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500', 'placeholder': 'Apellido', 'oninput': 'validarLetras("name")', 'maxlength': '50', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'validateLetters shadow-sm border text-sm rounded-lg block w-full p-2.5 bg-gray-600 border-gray-500 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500', 'placeholder': 'email@domain.com', 'oninput': 'validarLetras("name")', 'maxlength': '50', 'required': True}),
            'phone_number': forms.TextInput(attrs={'class': 'border text-sm rounded-lg block w-full p-2.5 bg-gray-600 border-gray-500 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500'}),
        }
        label_suffix = ' <span class="text-white">*</span>'


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

