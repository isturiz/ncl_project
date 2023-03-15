from django.shortcuts import render
from django.http import HttpResponse

from .models import Representative
from .models import Student

def index(request):
    return HttpResponse("Main page")

def home(request):
    return render(request, 'ncl/home/home.html')

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

def payment(request):
    return render(request, 'ncl/payment/payment.html')