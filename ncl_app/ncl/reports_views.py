from django.template.loader import render_to_string, get_template
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from weasyprint import HTML
import weasyprint

from django.db.models import Count


from datetime import datetime

from . import models


class ReportsView(HttpResponse):

    def index(request):
        representative_list = models.Representative.objects.all()

        context = {
            'list': representative_list,
        }
        return render(request, 'ncl/reports/report.html', context)

    def generate_pdf(request, report_type):

        properties = {
            'representative': {
                'th': ['nombre', 'apellido', 'email'],
            },
            'student': {
                'th': ['nombre', 'apellido', 'categoría edad', 'representante'],
            },
            'inscription': {
                'th': ['estudiante', 'cursos'],
            },
            'course': {
                'th': ['curso', 'profesor', 'estudiantes'],
            },
            'teacher': {
                'th': ['profesor', 'cursos', 'cantidad de estudiantes'],
            }
            

        }
        # Definir la vista en Django que renderice el contenido del PDF
        representative_list = models.Representative.objects.all()
        student_list = models.Student.objects.all()
        course_list = models.Course.objects.all()
        inscription_list = models.Inscription.objects.all()
        teacher_list = models.Teacher.objects.all()
        teachers = models.Teacher.objects.annotate(num_students=Count('course__inscription__student'))

        # Fecha reporte
        current_date = datetime.now().strftime('%d-%m-%Y')

        if report_type == 'representative':
            context = {
                'list': representative_list,
                'current_date': current_date,
                'title': 'Reporte de representantes',
                'report_type': 'representative',
                'properties': properties['representative'],

            }
            filename = 'reporte_representantes.pdf'

        elif report_type == 'student':
            context = {
                'list': student_list,
                'current_date': current_date,
                'title': 'Reporte de estudiantes',
                'report_type': 'student',
                'properties': properties['student'],
                'list_course': inscription_list,


                #'courses': courses,
            }
            filename = 'reporte_estudiantes.pdf'

        elif report_type == 'course':
            context = {
                'list': course_list,
                'current_date': current_date,
                'title': 'Reporte de cursos',
                'report_type': 'course',
                'properties': properties['course'],


            }
            filename = 'reporte_course.pdf'

        elif report_type == 'inscription':
            context = {
                'list': inscription_list,
                'current_date': current_date,
                'title': 'Reporte de inscripciones',
                'report_type': 'inscription',
                'properties': properties['inscription'],


            }
            filename = 'reporte_inscripciones.pdf'

        elif report_type == 'teacher':
            context = {
                'list': teacher_list,
                'current_date': current_date,
                'title': 'Reporte de profesores',
                'report_type': 'teacher',
                'properties': properties['teacher'],
                'teachers': teachers,

            }
            filename = 'reporte_profesores.pdf'
        else:
            pass
        #return render(request, 'ncl/report.html', context)

            # Tipo de reporte no válido, manejar el caso apropiado

        # Utilizar render_to_string para generar el contenido HTML del PDF
        html_string = render_to_string('ncl/report.html', context)

        # Crear un objeto BytesIO para almacenar el PDF generado
        pdf_file = BytesIO()

        # Generar el PDF utilizando WeasyPrint
        weasyprint.HTML(string=html_string).write_pdf(pdf_file)

        # Configurar la respuesta HTTP para devolver el PDF generado
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        response.write(pdf_file.getvalue())
        return response
    
    def test_report(request, report_type):
        properties = {
            'representative': {
                'th': ['nombre', 'apellido', 'email'],
            },
            'student': {
                'th': ['nombre', 'apellido', 'email'],
            },
            'inscription': {
                'th': ['estudiante', 'cursos'],
            },
            'course': {
                'th': ['curso', 'profesor', 'estudiantes'],
            }
            

        }
        # Definir la vista en Django que renderice el contenido del PDF
        representative_list = models.Representative.objects.all()
        student_list = models.Student.objects.all()
        course_list = models.Course.objects.all()
        inscription_list = models.Inscription.objects.all()
        teacher_list = models.Teacher.objects.all()

        current_date = datetime.now().strftime('%d-%m-%Y')

        if report_type == 'representative':
            context = {
                'list': representative_list,
                'current_date': current_date,
                'title': 'Reporte de representantes',
                'report_type': 'representative',
                'properties': properties['representative'],

            }
            filename = 'reporte_representantes.pdf'

        elif report_type == 'student':
            context = {
                'list': student_list,
                'current_date': current_date,
                'title': 'Reporte de estudiantes',
                'report_type': 'student',
                'properties': properties['student'],
            }
            filename = 'reporte_estudiantes.pdf'

        elif report_type == 'course':
            context = {
                'list': course_list,
                'current_date': current_date,
                'title': 'Reporte de cursos',
                'report_type': 'course',
                'properties': properties['course'],


            }
            filename = 'reporte_course.pdf'

        elif report_type == 'inscription':
            context = {
                'list': inscription_list,
                'current_date': current_date,
                'title': 'Reporte de inscripciones',
                'report_type': 'inscription',
                'properties': properties['inscription'],


            }
            filename = 'reporte_inscripciones.pdf'

        elif report_type == 'teacher':
            context = {
                'list': teacher_list,
                'current_date': current_date,
                'title': 'Reporte de profesores',
                'report_type': 'teacher',

            }
            filename = 'reporte_profesores.pdf'
        else:
            pass
        return render(request, 'ncl/report.html', context)
