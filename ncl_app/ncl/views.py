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

    if request.method == 'POST':
        register_form = RepresentativeForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('representative')
    else:
        register_form = RepresentativeForm()

    context = {
        'representative_list': representative_list,
        'register_form': register_form
    }
    return render(request, 'ncl/representative/representative.html', context)


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
    age_category_list = AgeCategory.objects.all()
    
    # if request.method == 'POST':
    #     print('Entrada al if')
    #     register_form = StudentForm(request.POST)
    #     if register_form.is_valid():
    #         register_form.save()
    #         return redirect('student')
    # else:
    #     print('Entrada al else')
    #     initial_values = {
    #         'age_category': age_category_list.first(),
    #         'representative': representative_list.first(),
    #     }
    #     register_form = StudentForm(initial=initial_values)

    context = {
        'student_list': student_list,
        'representative_list': representative_list,
        'age_category_list': age_category_list,
    }
    return render(request, 'ncl/student/student.html', context)

def add_student(request):
    if request.method == 'POST':
        print('Entrada al if add student')
        register_form = StudentForm(request.POST)
        print(register_form.errors)
        if register_form.is_valid():
            print('formulario válido student')
            register_form.save()
            print('formulario guardado student')
            return redirect('student')
        
    register_form = StudentForm()
    context = {
        'register_form': register_form
    }
    return render(request, 'ncl/forms/register_form_temp.html', context)


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = StudentForm(instance=student)
    context = {
        'student': student,
        'form': form,
    }
    return render(request, 'ncl/student/student.html', context)

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student')

# Teacher Views
def teacher(request):
    teacher_list = Teacher.objects.all()
    
    if request.method == 'POST':
        register_form = TeacherForm(request.POST)
        print("Contenido de POST:", request.POST)
        print(register_form)
        if register_form.is_valid():
            register_form.save()
            return redirect('teacher')
    else:
        register_form = TeacherForm()

    context = {
        'teacher_list': teacher_list,
        'register_form': register_form,
    }
    return render(request, 'ncl/teacher/teacher.html', context)


# Payment Views
def payment(request):
    payment_list = Payment.objects.all()
    total_income = payment_list.aggregate(Sum('amount'))['amount__sum']
    course_list = Course.objects.all()
    student_list = Student.objects.all()

    if request.method == 'POST':
        register_form = PaymentForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            return redirect('payment')
    else:
        register_form = PaymentForm()

    context = {
        'payment_list': payment_list,
        'total_income': total_income,
        'course_list': course_list,
        'student_list': student_list,
        'register_form': register_form,
    }
    return render(request, 'ncl/payment/payment.html', context)


# Course Views
# def course(request):
#     course_list = Course.objects.all()
#     teacher_list = Teacher.objects.all()

#     if request.method == 'POST':
#         form = CourseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('course')
#     else:
#         initial_values = {
#             'teacher': teacher_list.first(),
#         }
#         form = CourseForm(initial=initial_values)

#     context = {
#         'course_list': course_list,
#         'teacher_list': teacher_list,
#         'form': form,
#     }
#     return render(request, 'ncl/course/course.html', context)
def course(request):
    course_list = Course.objects.all()
    teacher_list = Teacher.objects.all()
    print("Contenido de POST:", request.POST)
    if request.method == 'POST':
        if 'register-form-submit' in request.POST:
            form = CourseForm(request.POST, prefix='register')
            print(form.is_valid())
            if form.is_valid():
                form.save()
                return redirect('course')
        elif 'edit-form-submit' in request.POST:
            form = CourseForm(request.POST, prefix='edit')
            if form.is_valid():
                form.save()
                return redirect('course')
    else:
        initial_values = {
            'teacher': teacher_list.first(),
        }
        register_form = CourseForm(initial=initial_values, prefix='register')
        edit_form = CourseForm(prefix='edit')
        context = {
            'course_list': course_list,
            'teacher_list': teacher_list,
            'register_form': register_form,
            'edit_form': edit_form,
        }
        return render(request, 'ncl/course/course.html', context)


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

def edit_course(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course.html', {'form': form})

def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('course')

# Inscription Views
def inscription(request):
    inscription_list = Inscription.objects.all()
    student_list = Student.objects.all()
    course_list = Course.objects.all()

    if request.method == 'POST':
        register_form = InscriptionForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('inscription')
    else:
        register_form = InscriptionForm()

    context = {
        'inscription_list': inscription_list,
        'student_list': student_list,
        'course_list': course_list,
        'register_form': register_form
    }
    return render(request, 'ncl/inscription/inscription.html', context)

