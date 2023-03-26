from django import forms
from .models import Student
from .models import Payment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'birthdate', 'age_category', 'representative')

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('student', 'payment_date', 'reference_number', 'amount', 'description')
