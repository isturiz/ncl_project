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

