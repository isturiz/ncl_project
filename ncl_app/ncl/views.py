from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum

from .models import Representative, Student
from .models import Teacher
from .models import Payment

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