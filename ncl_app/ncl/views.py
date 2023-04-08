from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Sum

from .models import Representative, Student
from .models import AgeCategory
from .models import Teacher
from .models import Payment
from .models import Course
from .models import Inscription

from .forms import StudentForm, RepresentativeForm, CourseForm, TeacherForm, InscriptionForm, PaymentForm

def index(request):
    return HttpResponse("Main page")

def home(request):
    total_student = Student.objects.count()
    total_income = Payment.objects.all().aggregate(Sum('amount'))['amount__sum']
    return render(request, 'ncl/home/home.html', {
        'total_student': total_student,
        'total_income': total_income
    })

# Representative Views
def representative(request):
    representative_list = Representative.objects.all()
    form = RepresentativeForm()

    if request.method == 'POST':
        form = RepresentativeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('representative')
    else:
        form = RepresentativeForm()

    context = {
        'representative_list': representative_list,
        'form': form
    }

    
    return render(request, 'ncl/representative/representative.html', context)

def add_representative(request):
    if request.method == 'POST':
        form = RepresentativeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('representative')
    else:
        form = RepresentativeForm()

    return render(request, 'ncl/representative/add_representative.html', {'form': form})

def edit_representative(request):
  if request.method == 'POST':
    id = request.POST.get('id')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone_number = request.POST.get('phone_number')

    representative = Representative.objects.get(id=id)
    representative.first_name = first_name
    representative.last_name = last_name
    representative.email = email
    representative.phone_number = phone_number
    representative.save()

    return redirect('representative')

  return render(request, 'representative/edit_representative.html')

def delete_representative(request, representative_id):
    representative = Representative.objects.get(id=representative_id)
    representative.delete()
    return redirect('representative')

# Student Views
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



# Teacher Views
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

# Payment Views
def payment(request):
    payment_list = Payment.objects.all()
    total_income = payment_list.aggregate(Sum('amount'))['amount__sum']
    course_list = Course.objects.all()
    student_list = Student.objects.all()

    return render(request, 'ncl/payment/payment.html', {
        'payment_list': payment_list,
        'total_income': total_income,
        'course_list': course_list,
        'student_list': student_list
    })

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form': form})

# Course Views
def course(request):
    course_list = Course.objects.all()
    teacher_list = Teacher.objects.all()

    return render(request, 'ncl/course/course.html', {
        'course_list': course_list,
        'teacher_list': teacher_list,
        
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


# def edit_course(request):
#   if request.method == 'POST':
#     id = request.POST.get('id')
#     name = request.POST.get('name')
#     teacher = request.POST.get('teacher')

#     course = Course.objects.get(id=id)
#     course.name = name
#     course.teacher = teacher
#     course.save()

#     return redirect('course')

#   return render(request, 'edit_course.html')

def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course.html', {'form': form})

def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('course')

# Inscription Views
def inscription(request):
    inscription_list = Inscription.objects.all()
    student_list = Student.objects.all()
    course_list = Course.objects.all()

    return render(request, 'ncl/inscription/inscription.html', {
        'inscription_list': inscription_list,
        'student_list': student_list,
        'course_list': course_list,
    })

def add_inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscription')
    else:
        form = InscriptionForm()
    return render(request, 'inscription.html', {'form': form})