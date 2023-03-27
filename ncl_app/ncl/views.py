from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Sum

from .models import Representative, Student
from .models import AgeCategory
from .models import Teacher
from .models import Payment
from .models import Course

from .forms import StudentForm, RepresentativeForm, CourseForm, TeacherForm

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
    representative_list = Representative.objects.all()
    age_category = AgeCategory.objects.all()
    return render(request, 'ncl/student/student.html', {
        'student_list': student_list,
        'representative_list': representative_list,
        'age_category': age_category
    })

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


def representative(request):
    representative_list = Representative.objects.all()
    return render(request, 'ncl/representative/representative.html', {
        'representative_list': representative_list
    })

def add_representative(request):
    if request.method == 'POST':
        form = RepresentativeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('representative')
    else:
        form = RepresentativeForm()
    return render(request, 'add_representative.html', {'form': form})

def teacher(request):
    teacher_list = Teacher.objects.all()
    return render(request, 'ncl/teacher/teacher.html', {
        'teacher_list': teacher_list
    })

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher')
    else:
        form = RepresentativeForm()
    return render(request, 'add_teacher.html', {'form': form})

def payment(request):
    payment_list = Payment.objects.all()
    total_income = payment_list.aggregate(Sum('amount'))['amount__sum']
    return render(request, 'ncl/payment/payment.html', {
        'payment_list': payment_list,
        'total_income': total_income
    })

def course(request):
    course_list = Course.objects.all()
    return render(request, 'ncl/course/course.html', {
        'course_list': course_list
    })

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course')
    else:
        form = CourseForm()
    return render(request, 'course.html', {'form': form})