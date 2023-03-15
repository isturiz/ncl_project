from django.contrib import admin

from .models import Representative, Student
from .models import Teacher
from .models import Payment


# Las clases sirven para definir los atributos que se mostrarán en locahost/8000/admin/
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'representative', 'age_category')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'payment_date', 'reference_number', 'amount', 'description')

admin.site.register(Representative)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Payment, PaymentAdmin)