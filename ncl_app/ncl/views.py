from django.shortcuts import render
from django.http import HttpResponse

from .models import Representative, Student
from .models import Teacher

def index(request):
    return HttpResponse("Main page")

def home(request):
    total_student = Student.objects.count()
    return render(request, 'ncl/home/home.html', 
        {'total_student': total_student}
    )

def student(request):
    student_list = Student.objects.all()
    return render(request, 'ncl/student/student.html', {
        "student_list": student_list
    })


def representative(request):
    representative_list = Representative.objects.all()
    return render(request, 'ncl/representative/representative.html', {
        "representative_list": representative_list
    })

def teacher(request):
    teacher_list = Teacher.objects.all()
    return render(request, 'ncl/teacher/teacher.html', {
        "teacher_list": teacher_list
    })

def payment(request):
    payment_list = payment.objects.all()
    return render(request, 'ncl/payment/payment.html', {
        "payment_list": payment_list
    })