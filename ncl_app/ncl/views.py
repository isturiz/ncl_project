from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Sum

from .models import Representative, Student
from .models import Teacher
from .models import Payment

from .forms import StudentForm, PaymentForm

def index(request):
    return HttpResponse("Main page")

def home(request):
    total_student = Student.objects.count()
    total_income = Payment.objects.all().aggregate(Sum('amount'))['amount__sum']
    return render(request, 'ncl/home/home.html', {
        'total_student': total_student,
        'total_income': total_income
    })

def student(request):
    student_list = Student.objects.all()
    return render(request, 'ncl/student/student.html', {
        'student_list': student_list
    })

def add_student_modal(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():

            # Obtener el objeto Representative de la base de datos
            representative_id = form.cleaned_data['representative']
            representative = get_object_or_404(Representative, pk=representative_id)
            # Guardar el objeto Student en la base de datos
            student = form.save(commit=False)
            student.representative = representative
            student.save()

            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'add_student_modal.html', {'form': form, 'representatives': student.representative})

def representative(request):
    representative_list = Representative.objects.all()
    return render(request, 'ncl/representative/representative.html', {
        'representative_list': representative_list
    })

def teacher(request):
    teacher_list = Teacher.objects.all()
    return render(request, 'ncl/teacher/teacher.html', {
        'teacher_list': teacher_list
    })

def payment(request):
    payment_list = Payment.objects.all()
    total_income = payment_list.aggregate(Sum('amount'))['amount__sum']
    return render(request, 'ncl/payment/payment.html', {
        'payment_list': payment_list,
        'total_income': total_income
    })

def add_payment_modal(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            new_paymnent = form.save()

            return redirect('payment_list')
    else:
        form = PaymentForm()

    return render(request, 'add_payment_modal.html', {'form': form})
