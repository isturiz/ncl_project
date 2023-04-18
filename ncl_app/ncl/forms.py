from django import forms
from .models import Student, Representative, Course, Teacher, Inscription, Payment, AgeCategory

class StudentForm(forms.ModelForm):

    age_category = forms.ModelChoiceField(queryset=AgeCategory.objects.all(), empty_label=None)
    representative = forms.ModelChoiceField(queryset=Representative.objects.all(), empty_label=None)

    class Meta:
        model = Student
        fields = [
            'first_name', 
            'last_name',
            'email',
            'phone_number',
            'address',
            'birthdate',
            'age_category',
            'representative',
        ]
        labels = {
            'first_name': 'Nombre', 
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'phone_number': 'Número de teléfono',
            'address': 'Dirección',
            'birthdate': 'Fecha de nacimiento',
            'age_category': 'Categoría de edad',
            'representative': 'Representante',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@domain.com'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '04121555551'}),
            'address': forms.TextInput(attrs={'placeholder': 'Calle, número de casa'}),
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'age_category': forms.Select(),
            'representative': forms.Select(),
        }

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
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@domain.com'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '04121555551'}),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'name', 
            'teacher'
            ]
        labels = {
            'name': 'Nombre', 
            'teacher': 'Profesores', 
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre del curso'}),
            'teacher': forms.SelectMultiple(attrs={'multiple': True}),
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name', 
            'last_name',
            'email',
            'phone_number',
            'address',
        ]
        labels = {
            'first_name': 'Nombre', 
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'phone_number': 'Número de teléfono',
            'address': 'Dirección',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@domain.com'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '04121555551'}),
            'address': forms.TextInput(attrs={'placeholder': 'Calle, número de casa'}),
        }

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'student', 
            'payment_date',
            'reference_number',
            'amount',
            'description',
            'course',
        ]
        labels = {
            'student': 'Estudiante', 
            'payment_date': 'Fecha del pago',
            'reference_number': 'Número de referencia',
            'amount': 'Monto',
            'description': 'Descripción',
            'course': 'Curso',
        }
        widgets = {
            'student': forms.Select(),
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
            'reference_number': forms.TextInput(attrs={'placeholder': '0000538'}),
            'amount': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'placeholder': '50'}),
            'description': forms.TextInput(attrs={'placeholder': 'Descripción'}),
            'course': forms.SelectMultiple(attrs={'multiple': True}),
        }

