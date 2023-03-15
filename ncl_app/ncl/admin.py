from django.contrib import admin

from .models import Representative, Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'representative')

admin.site.register(Representative)
admin.site.register(Student, StudentAdmin)