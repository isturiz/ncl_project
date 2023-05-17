from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Sum, Count

from django.urls import reverse

from .models import Representative, Student
from .models import AgeCategory
from .models import Teacher
from .models import Payment
from .models import Course
from .models import Inscription

from .forms import StudentForm, RepresentativeForm, CourseForm, TeacherForm, InscriptionForm, PaymentForm

from .auth_views import *


from django.template.loader import render_to_string
import weasyprint
from io import BytesIO

def index(request):
    return HttpResponse("Main page")

def home(request):
    total_student = Student.objects.count()
    total_income = Payment.objects.all().aggregate(Sum('amount'))['amount__sum']
    return render(request, 'ncl/home/home.html', {
        'total_student': total_student,
        'total_income': total_income
    })

class RepresentativeViews(HttpResponse):
    def index(request):
        representative_list = Representative.objects.all()

        representative_data = [
            {
                'title': 'Canto',
                'subtitle': None,
                'color': 'text-red-400',
            },
            {
                'title': 'Piano',
                'subtitle': None,
                'color': 'text-yellow-400',
            },
            {
                'title': 'Cuatro',
                'subtitle': None,
                'color': 'text-orange-400',
            },
            ]
        #for i, course in enumerate(representative_list):
        #    representatives = course.teacher.all()
        #    representative_data[i]['subtitle'] = representatives.count()

        context = {
            'representative_list': representative_list,
            'representative_data': representative_data,
        }
        return render(request, 'ncl/representative/representative.html', context)
    
    def register_form(request):
        register_form = RepresentativeForm()
        url_process = 'register_form_process__representative'
        return render(request, 'ncl/forms/register.html', {'register_form': register_form, 'url_process': url_process})
    
    def register_form_process(request):
        register_form = RepresentativeForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        return redirect('representative')

    def edit_form(request, representative_id):
        representative = Representative.objects.get(id=representative_id)
        edit_form = RepresentativeForm(instance=representative)

        url_process = reverse('edit_form_process__representative', args=[representative.id])
        context = {
            'edit_form': edit_form,
            'representative': representative,
            'url_process': url_process,
        }
        return render(request, 'ncl/forms/edit.html', context)
    
    def edit_form_process(request, representative_id):
        representative = Representative.objects.get(pk=representative_id)
        edit_form = RepresentativeForm(request.POST, instance=representative)
        if edit_form.is_valid():
            edit_form.save()
        return redirect('representative')


def delete_representative(request, representative_id):
    representative = Representative.objects.get(id=representative_id)
    representative.delete()
    return redirect('representative')

# Student Views
class StudentViews(HttpResponse):
    def index(request):
        student_list = Student.objects.all()
        representative_list = Representative.objects.all()
        age_category_list = AgeCategory.objects.all()
        student_data = [
        {
            'title': 'Canto',
            # 'num_teachers': teacher_list.filter(subject='Canto').count(),
            'color': 'text-red-400',
        },
        {
            'title': 'Piano',
            # 'num_teachers': teacher_list.filter(subject='Piano').count(),
            'color': 'text-yellow-400',
        },
        {
            'title': 'Cuatro',
            # 'num_teachers': teacher_list.filter(subject='Cuatro').count(),
            'color': 'text-orange-400',
        },
        ]
        item_property = {
            'first_name': 'nombre',
            'last_name': 'apellido',
            'phone': 'teléfono',
            'email': 'correo',
            'representative': 'representante',
        }

        context = {
            'student_list': student_list,
            'representative_list': representative_list,
            'age_category_list': age_category_list,
            'student_data': student_data,
            'item_property': item_property,
        }
        return render(request, 'ncl/student/student.html', context)
    
    def register_form(request):
        register_form = StudentForm()
        url_process = 'register_form_process__student'

        context = {
            'register_form': register_form,
            'url_process': url_process
        }

        return render(request, 'ncl/forms/register.html', context)
    
    def register_form_process(request):
        register_form = StudentForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        return redirect('student')

    def edit_form(request, student_id):
        student = Student.objects.get(id=student_id)
        edit_form = StudentForm(instance=student)

        url_process = reverse('edit_form_process__student', args=[student.id])
        context = {
            'edit_form': edit_form,
            'student': student,
            'url_process': url_process,
        }
        return render(request, 'ncl/forms/edit.html', context)
    
    def edit_form_process(request, student_id):
        student = Student.objects.get(pk=student_id)
        edit_form = StudentForm(request.POST, instance=student)
        if edit_form.is_valid():
            edit_form.save()
        return redirect('student')

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('student')

class TeacherViews(HttpResponse):
    def index(request):
        teacher_list = Teacher.objects.all()
        courses = Course.objects.all()
        teacher_data = [
        {
            'title': 'Canto',
            'subtitle': None,
            'color': 'text-red-400',
        },
        {
            'title': 'Piano',
            'subtitle': None,
            'color': 'text-yellow-400',
        },
        {
            'title': 'Cuatro',
            'subtitle': None,
            'color': 'text-orange-400',
        },
        ]
        for i, course in enumerate(courses):
            teachers = course.teacher.all()
            teacher_data[i]['subtitle'] = teachers.count()
        context = {
        'teacher_list': teacher_list,
        'teacher_data': teacher_data,
    }
        return render(request, 'ncl/teacher/teacher.html', context)

    def register_form(request):
        register_form = TeacherForm()
        url_process = 'register_form_process__teacher'

        context = {
            'register_form': register_form,
            'url_process': url_process
        }

        return render(request, 'ncl/forms/register.html', context)
    
    def register_form_process(request):
        register_form = TeacherForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        return redirect('teacher')

    def edit_form(request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        edit_form = TeacherForm(instance=teacher)

        url_process = reverse('edit_form_process__teacher', args=[teacher.id])
        context = {
            'edit_form': edit_form,
            'teacher': teacher,
            'url_process': url_process,
        }
        return render(request, 'ncl/forms/edit.html', context)
    
    def edit_form_process(request, teacher_id):
        teacher = Teacher.objects.get(pk=teacher_id)
        edit_form = TeacherForm(request.POST, instance=teacher)
        if edit_form.is_valid():
            edit_form.save()
        return redirect('teacher')

def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    teacher.delete()
    return redirect('teacher')

class PaymentViews(HttpResponse):
    def index(request):
        payment_list = Payment.objects.all()
        total_income = payment_list.aggregate(Sum('amount'))['amount__sum']
        course_list = Course.objects.all()
        student_list = Student.objects.all()
        context = {
        'payment_list': payment_list,
        'total_income': total_income,
        'course_list': course_list,
        'student_list': student_list,
    }
        return render(request, 'ncl/payment/payment.html', context)
    
    def register_form(request):
        register_form = PaymentForm()
        url_process = 'register_form_process__payment'

        context = {
            'register_form': register_form,
            'url_process': url_process
        }

        return render(request, 'ncl/forms/register.html', context)
    
    def register_form_process(request):
        register_form = PaymentForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        return redirect('payment')

    def edit_form(request, payment_id):
        payment = Payment.objects.get(id=payment_id)
        edit_form = PaymentForm(instance=payment)

        url_process = reverse('edit_form_process__payment', args=[payment.id])
        context = {
            'edit_form': edit_form,
            'payment': payment,
            'url_process': url_process,
        }
        return render(request, 'ncl/forms/edit.html', context)
    
    def edit_form_process(request, payment_id):
        payment = Payment.objects.get(pk=payment_id)
        edit_form = PaymentForm(request.POST, instance=payment)
        if edit_form.is_valid():
            edit_form.save()
        return redirect('payment')
    
def delete_payment(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    payment.delete()
    return redirect('payment')


class InscriptionViews(HttpResponse):
    def index(request):
        inscription_list = Inscription.objects.all()
        student_list = Student.objects.all()
        course_list = Course.objects.all()
        context = {
            'inscription_list': inscription_list,
            'student_list': student_list,
            'course_list': course_list,
        }
        return render(request, 'ncl/inscription/inscription.html', context)
    
    def register_form(request):
        register_form = PaymentForm()
        url_process = 'register_form_process__inscription'

        context = {
            'register_form': register_form,
            'url_process': url_process
        }

        return render(request, 'ncl/forms/register.html', context)
    
    def register_form_process(request):
        register_form = InscriptionForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        return redirect('inscription')

    def edit_form(request, inscription_id):
        inscription = Inscription.objects.get(id=inscription_id)
        edit_form = InscriptionForm(instance=inscription)

        url_process = reverse('edit_form_process__inscription', args=[inscription.id])
        context = {
            'edit_form': edit_form,
            'inscription': inscription,
            'url_process': url_process,
        }
        return render(request, 'ncl/forms/edit.html', context)
    
    def edit_form_process(request, inscription_id):
        inscription = Inscription.objects.get(pk=inscription_id)
        edit_form = InscriptionForm(request.POST, instance=inscription)
        if edit_form.is_valid():
            edit_form.save()
        return redirect('inscription')

def delete_inscription(request, inscription_id):
    inscription = Inscription.objects.get(id=inscription_id)
    inscription.delete()
    return redirect('inscription')

class CourseViews(HttpResponse):
    def index(request):
        course_list = Course.objects.all()
        course_list_card = (
            Course.objects.annotate(num_teachers=Count('teacher'))
            .order_by('-num_teachers')[:3]
        )
        teacher_list = Teacher.objects.all()
        course_data = [
        {
            'title': 'Vacío',
            'subtitle': None,
            'color': 'text-red-400',
        },
        {
            'title': 'Vacío',
            'subtitle': None,
            'color': 'text-yellow-400',
        },
        {
            'title': 'Vacío',
            'subtitle': None,
            'color': 'text-orange-400',
        },
        ]
        for i, course in enumerate(course_list_card):
            if i >= 3:
                break
            teachers = course.teacher.all()
            course_data[i]['title'] = course.name
            course_data[i]['subtitle'] = teachers.count()
        
        context = {
            'course_list': course_list,
            'teacher_list': teacher_list,
            'course_data': course_data,
        }
        return render(request, 'ncl/course/course.html', context)
    
    def register_form(request):
        register_form = CourseForm()
        url_process = 'register_form_process__course'

        context = {
            'register_form': register_form,
            'url_process': url_process
        }

        return render(request, 'ncl/forms/register.html', context)
    
    def register_form_process(request):
        register_form = CourseForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        return redirect('course')

    def edit_form(request, course_id):
        course = Course.objects.get(id=course_id)
        edit_form = CourseForm(instance=course)

        url_process = reverse('edit_form_process__course', args=[course.id])
        context = {
            'edit_form': edit_form,
            'course': course,
            'url_process': url_process,
        }
        return render(request, 'ncl/forms/edit.html', context)
    
    def edit_form_process(request, course_id):
        course = Course.objects.get(pk=course_id)
        edit_form = CourseForm(request.POST, instance=course)
        if edit_form.is_valid():
            edit_form.save()
        return redirect('course')

def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('course')

class AnalyticsView(HttpResponse):

    def index(request):
        representative_list = Representative.objects.all()

        context = {
            'representative_list': representative_list,
        }
        return render(request, 'ncl/analytics/analytics.html', context)

    def generar_pdf(request):
        # Definir la vista en Django que renderice el contenido del PDF
        representative_list = Representative.objects.all()
        context = {
            'representative_list': representative_list,
        }


        # Utilizar render_to_string para generar el contenido HTML del PDF
        html_string = render_to_string('ncl/report.html', context)

        # Crear un objeto BytesIO para almacenar el PDF generado
        pdf_file = BytesIO()

        # Generar el PDF utilizando WeasyPrint
        weasyprint.HTML(string=html_string).write_pdf(pdf_file)

        # Configurar la respuesta HTTP para devolver el PDF generado
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="tu_reporte.pdf"'
        response.write(pdf_file.getvalue())
        return response
    