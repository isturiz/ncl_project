from django.contrib import admin

from .models import Representative, Student
from .models import Teacher

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'representative')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')


admin.site.register(Representative)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)