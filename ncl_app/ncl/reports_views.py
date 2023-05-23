from django.template.loader import render_to_string, get_template
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from weasyprint import HTML
import weasyprint


from datetime import datetime

from . import models


class ReportsView(HttpResponse):

    def index(request):
        representative_list = models.Representative.objects.all()

        context = {
            'list': representative_list,
        }
        return render(request, 'ncl/reports/report.html', context)

    def generar_pdf(request):
        # Definir la vista en Django que renderice el contenido del PDF
        representative_list = models.Representative.objects.all()
        current_date = datetime.now().strftime('%d-%m-%Y')
        context = {
            'list': representative_list,
            'current_date': current_date,
            'title': 'Reportes de prueba',
        }

        # Utilizar render_to_string para generar el contenido HTML del PDF
        html_string = render_to_string('ncl/report.html', context)

        # Crear un objeto BytesIO para almacenar el PDF generado
        pdf_file = BytesIO()

        # Generar el PDF utilizando WeasyPrint
        weasyprint.HTML(string=html_string).write_pdf(pdf_file)

        # Configurar la respuesta HTTP para devolver el PDF generado
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
        response.write(pdf_file.getvalue())
        return response
    
    def test_report(request):
        representative_list = models.Representative.objects.all()
        current_date = datetime.now().strftime('%d-%m-%Y')
        context = {
            'list': representative_list,
            'current_date': current_date,
            'title': 'Reportes de prueba',
        }
        return render(request, 'ncl/report.html', context)
